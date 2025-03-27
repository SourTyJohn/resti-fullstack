from typing import Any, Type, Generic, TypeVar
from collections.abc import Sequence
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.interfaces import ORMOption

from app.database.models.base import DecBase


generic_model = TypeVar(
    name="generic_model",
    bound=DecBase,
    covariant=True,
    contravariant=False
)


class BaseDAO(Generic[generic_model]):
    def __init__(self, model: Type[generic_model], session: AsyncSession):
        self.model = model
        self.session = session

    async def _get_by_pk(
            self,
            pk: uuid.UUID,
            options: Sequence[ORMOption] | None = None,
            populate_existing: bool = False
        ) -> generic_model | None:
        result = await self.session.get(
            self.model, pk, options=options, populate_existing=populate_existing
        )
        return result

    async def _get_all(
            self,
            options: Sequence[ORMOption] = ()
        ) -> Sequence[generic_model]:
        result = await self.session.scalars(
            select(self.model).options(*options)
        )
        return result.all()
    
    async def _save(self, obj: DecBase):
        self.session.add(obj)
    
    async def _delete(self, obj: DecBase):
        await self.session.delete(obj)
