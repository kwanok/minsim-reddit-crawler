from pydantic.v1 import BaseSettings


class Config(BaseSettings):
    REDDIT_CLIENT_ID: str = "3c197967ac7ccc836c6c0adea23698c5"
    REDDIT_CLIENT_SECRET: str = "secret"
    REDDIT_USERNAME: str = ""
    REDDIT_PASSWORD: str = ""

    API_HOST: str = "localhost:8100"

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0

    @property
    def REDIS_URI(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "APP_"


config = Config()
