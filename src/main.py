import asyncio

from src.client.client import RedditClient
from src.config.config import Config


async def main():
    config = Config()

    reddit_client = RedditClient(config=config)

    async with asyncio.TaskGroup() as tg:
        tg.create_task(reddit_client.start("all"))


if __name__ == "__main__":
    asyncio.run(main())
