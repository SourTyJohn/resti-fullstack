from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
    AsyncSession
)


def create_engine(db_uri: str) -> AsyncEngine:
    __engine: AsyncEngine = create_async_engine(
        url=db_uri,
        echo=True
    )
    return __engine


def create_session_maker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(engine, expire_on_commit=False)
