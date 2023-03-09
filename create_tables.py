from core.configs import settings
from core.databases import engine


async def create_tables() -> None:
    import models.__all__models

    print('creating tables')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('created tables')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())
