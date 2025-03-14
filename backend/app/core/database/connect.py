from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from fastapi import Depends
from app.config import config
from functools import lru_cache
from typing import Annotated


@lru_cache()
def get_engine() -> AsyncEngine:
    __db_uri = str( config().DB_URI )
    __engine: AsyncEngine = create_async_engine(url=__db_uri)
    return __engine


AsyncEngineDep = Annotated[
    AsyncEngine,
    Depends(get_engine)
]
