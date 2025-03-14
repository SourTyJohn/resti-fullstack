from typing import Any, Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import DecBase


class BaseRepository:
    model: Type[DecBase] # define in subclases
    __session: AsyncSession  # pass in __init__

    def __init__(self, session: AsyncSession):
        self.__session = session

    async def get(self, pk: int) -> Any | None:
        result = await self.__session.execute(
            select(self.model).where(self.model.id == pk)
        )
        return result.fetchone()
    
    async def create(self, data: Any) -> Any:
        obj = self.model( **data.model_dump() )
        self.__session.add(obj)
        return obj

    async def update(self, data: Any) -> Any:
        raise NotImplementedError
    
    async def delete(self, pk: int) -> None:
        raise NotImplementedError
