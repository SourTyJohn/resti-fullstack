import uuid

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel


class IDMixin:
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class CUTimeMixin:
    