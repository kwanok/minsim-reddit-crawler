import asyncio
import logging

import asyncpraw as praw
import grpc
from asyncprawcore import TooManyRequests

from src.config.config import Config
from src.redis.client import RedisClient
from src.redis.queue import RedisPubSub, Channel
from src.service.comment import comment_pb2, comment_pb2_grpc
from src.service.post import post_pb2_grpc, post_pb2


def new_comment_request(comment):
    return comment_pb2.NewCommentRequest(
        id=str(comment.id),
        author=str(comment.author),
        content=str(comment.body),
        subreddit=str(comment.subreddit),
        subreddit_id=str(comment.subreddit_id),
        created_at=int(comment.created_utc),
    )


def new_post_request(post):
    return post_pb2.NewPostRequest(
        id=str(post.id),
        author=str(post.author),
        title=str(post.title),
        content=str(post.selftext),
        subreddit=str(post.subreddit),
        created_at=int(post.created_utc),
        url=str(post.url),
    )


class RedditClient:
    def __init__(self, config: Config):
        self.reddit = praw.Reddit(
            client_id=config.REDDIT_CLIENT_ID,
            client_secret=config.REDDIT_CLIENT_SECRET,
            user_agent=(
                f"python:{config.REDDIT_CLIENT_ID}:0.0.1"
                f"(by /u/{config.REDDIT_USERNAME})"
            ),
            password=config.REDDIT_PASSWORD,
            username=config.REDDIT_USERNAME,
        )
        self.reddit.read_only = True
        self.subreddit = None
        self.api_host = config.API_HOST
        self.failed_queue = RedisPubSub(RedisClient(config).client())

    async def set_subreddit(self, subreddit):
        self.subreddit = await self.reddit.subreddit(subreddit)

    async def start(self, subreddit):
        await self.set_subreddit(subreddit)

        async with asyncio.TaskGroup() as tg:
            tg.create_task(self.get_subreddit_comment_stream(subreddit))
            tg.create_task(self.get_subreddit_submission_stream(subreddit))
            tg.create_task(self.subscribe_failed_queue(Channel.Comment))
            tg.create_task(self.subscribe_failed_queue(Channel.Post))

    async def get_subreddit_comment_stream(self, subreddit):
        logging.info(f"getting subreddit stream for {subreddit}")

        with grpc.insecure_channel(self.api_host) as channel:
            try:
                async for comment in self.subreddit.stream.comments(skip_existing=True):
                    stub = comment_pb2_grpc.CommentStub(channel)

                    try:
                        stub.NewComment(new_comment_request(comment))
                    except Exception as e:
                        await self.failed_queue.publish(
                            channel=Channel.Comment, message=str(comment.id)
                        )

                        logging.error(e)
                        continue
            except TooManyRequests:
                logging.error("too many requests, sleeping for 60 seconds")
                await asyncio.sleep(60)
                return await self.get_subreddit_comment_stream(subreddit)

    async def get_subreddit_submission_stream(self, subreddit):
        logging.info(f"getting subreddit stream for {subreddit}")

        with grpc.insecure_channel(self.api_host) as channel:
            try:
                async for submission in self.subreddit.stream.submissions(skip_existing=True):
                    stub = post_pb2_grpc.PostStub(channel)

                    try:
                        stub.NewPost(new_post_request(submission))
                    except Exception as e:
                        await self.failed_queue.publish(
                            channel=Channel.Post, message=str(submission.id)
                        )

                        logging.error(e)
                        continue
            except TooManyRequests:
                logging.error("too many requests, sleeping for 60 seconds")
                await asyncio.sleep(60)
                return await self.get_subreddit_submission_stream(subreddit)

    async def subscribe_failed_queue(self, channel: Channel):
        logging.info(f"subscribing to failed queue for {channel}")
        pubsub = await self.failed_queue.subscribe(channel=channel)

        async for message in pubsub.listen():
            if message["type"] != "message":
                continue

            if channel == Channel.Comment:
                await self.retry_new_comment(message["data"].decode("utf-8"))
            elif channel == Channel.Post:
                await self.retry_new_post(message["data"].decode("utf-8"))

    async def retry_new_comment(self, comment_id) -> bool:
        try:
            comment = await self.reddit.comment(comment_id)
        except TooManyRequests:
            await asyncio.sleep(60)
            return await self.retry_new_comment(comment_id)

        with grpc.insecure_channel(self.api_host) as channel:
            stub = comment_pb2_grpc.CommentStub(channel)

            try:
                stub.NewComment(new_comment_request(comment))
                logging.info(f"successfully published comment {comment.id}")
            except Exception as e:
                await self.failed_queue.publish(
                    channel=Channel.Comment, message=str(comment.id)
                )

                logging.error(e)
                return False

            return True

    async def retry_new_post(self, post_id) -> bool:
        try:
            post = await self.reddit.submission(post_id)
        except TooManyRequests:
            await asyncio.sleep(60)
            return await self.retry_new_post(post_id)

        with grpc.insecure_channel(self.api_host) as channel:
            stub = post_pb2_grpc.PostStub(channel)

            try:
                stub.NewPost(new_post_request(post))
                logging.info(f"successfully published post {post.id}")
            except Exception as e:
                await self.failed_queue.publish(
                    channel=Channel.Post, message=str(post.id)
                )

                logging.error(e)
                return False

            return True
