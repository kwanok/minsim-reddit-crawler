from enum import Enum

import redis.asyncio as async_redis
from redis.asyncio.client import PubSub


class Channel(str, Enum):
    Submission = "submission"
    Comment = "comment"


class RedisPubSub:
    def __init__(self, redis_client: async_redis.Redis):
        self.redis_client = redis_client

    async def publish(self, channel: Channel, message: str):
        await self.redis_client.publish(channel, message)

    async def subscribe(self, channel: Channel) -> PubSub:
        pubsub = self.redis_client.pubsub()
        await pubsub.subscribe(channel)

        return pubsub
