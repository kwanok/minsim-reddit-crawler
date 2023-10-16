import redis.asyncio as async_redis
from redis import BusyLoadingError
from redis.asyncio.retry import Retry
from redis.backoff import ExponentialBackoff
from src.config.config import Config


class RedisClient:
    def __init__(self, config: Config):
        self.pool = async_redis.ConnectionPool.from_url(config.REDIS_URI)

    def client(self) -> async_redis.Redis:
        # Backoff: 실패할 때 마다 재시도 간격을 늘린다
        # 0.008초 부터 최대 0.512초 까지 10번 재시도
        retry = Retry(ExponentialBackoff(), 10)

        return async_redis.Redis(
            connection_pool=self.pool,
            retry=retry,
            retry_on_error=[
                BusyLoadingError,
                ConnectionError,
                TimeoutError,
            ],
        )
