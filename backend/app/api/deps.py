from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from app.core.database import AsyncEngineDep
from typing import AsyncGenerator, Any, Annotated
from functools import lru_cache

from fastapi import Depends



@lru_cache()
def get_session_maker(__engine: AsyncEngineDep) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(__engine, expire_on_commit=False)


SessionMakerDep = Annotated[
    async_sessionmaker[AsyncSession], 
    Depends(get_session_maker)
]


async def make_async_session(session_maker: SessionMakerDep) -> AsyncGenerator[AsyncSession, Any]:
    async with session_maker() as session:
        yield session


SessionDep = Annotated[
    AsyncSession,
    Depends(make_async_session)
]
