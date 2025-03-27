from datetime import datetime

from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
import uuid


class DecBase(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id:         Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] =  mapped_column(default=func.now())
    updated_at: Mapped[datetime] =  mapped_column(default=func.now(), onupdate=func.now())

    @classmethod
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'

    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)
