from typing import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, AsyncEngine

from app.database.connection import create_engine, create_session_maker
from app.config import Settings


class DatabaseProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_engine(self, config: Settings) -> AsyncIterable[AsyncEngine]:
        engine = create_engine(config.DB_URI)
        yield engine
        await engine.dispose(True)

    @provide
    def get_sessionmaker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return create_session_maker(engine)

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self, session_factory: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with session_factory() as session:
            yield session
