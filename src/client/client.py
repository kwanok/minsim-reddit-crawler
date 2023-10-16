import asyncio
import logging

import asyncpraw as praw
import grpc
from asyncprawcore import TooManyRequests

from src.config.config import Config
from src.redis.client import RedisClient
from src.redis.queue import Channel, RedisPubSub
from src.service.comment import comment_pb2, comment_pb2_grpc
from src.service.submission import submission_pb2, submission_pb2_grpc


def new_comment_request(comment):
    return comment_pb2.NewCommentRequest(
        id=str(comment.id),
        author=str(comment.author),
        body=str(comment.body),
        body_html=str(comment.body_html),
        created_utc=int(comment.created_utc),
        distinguished=str(comment.distinguished),
        edited=bool(comment.edited),
        is_submitter=comment.is_submitter,
        link_id=str(comment.link_id),
        parent_id=str(comment.parent_id),
        permalink=str(comment.permalink),
        stickied=bool(comment.stickied),
        submission=str(comment.submission),
        subreddit=str(comment.subreddit),
        subreddit_id=str(comment.subreddit_id),
    )


def new_submission_request(submission):
    return submission_pb2.NewSubmissionRequest(
        id=str(submission.id),
        author=str(submission.author),
        author_flair_text=str(submission.author_flair_text),
        clicked=bool(submission.clicked),
        created_utc=int(submission.created_utc),
        is_original_content=bool(submission.is_original_content),
        is_self=bool(submission.is_self),
        link_flair_text=str(submission.link_flair_text),
        locked=bool(submission.locked),
        name=str(submission.name),
        num_comments=int(submission.num_comments),
        over_18=bool(submission.over_18),
        permalink=str(submission.permalink),
        score=int(submission.score),
        selftext=str(submission.selftext),
        subreddit=str(submission.subreddit),
        subreddit_id=str(submission.subreddit_id),
        title=str(submission.title),
        upvote_ratio=float(submission.upvote_ratio),
        url=str(submission.url),
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
            tg.create_task(self.subscribe_failed_queue(Channel.Submission))

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
                async for submission in self.subreddit.stream.submissions(
                    skip_existing=True
                ):
                    stub = submission_pb2_grpc.SubmissionStub(channel)

                    try:
                        stub.NewSubmission(new_submission_request(submission))
                    except Exception as e:
                        await self.failed_queue.publish(
                            channel=Channel.Submission, message=str(submission.id)
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
            elif channel == Channel.Submission:
                await self.retry_new_submission(message["data"].decode("utf-8"))

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

    async def retry_new_submission(self, submission_id) -> bool:
        try:
            submission = await self.reddit.submission(submission_id)
        except TooManyRequests:
            await asyncio.sleep(60)
            return await self.retry_new_submission(submission_id)

        with grpc.insecure_channel(self.api_host) as channel:
            stub = submission_pb2_grpc.SubmissionStub(channel)

            try:
                stub.NewSubmission(new_submission_request(submission))
                logging.info(f"successfully published submission {submission.id}")
            except Exception as e:
                await self.failed_queue.publish(
                    channel=Channel.Submission, message=str(submission.id)
                )

                logging.error(e)
                return False

            return True
