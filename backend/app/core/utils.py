from typing import Type, TypeVar
from pydantic import BaseModel
from app.database.models.base import DecBase


T = TypeVar('T', bound=BaseModel)


def to_pydantic(db_object: DecBase, pydantic_model: Type[T]) -> T:
    return pydantic_model(**db_object.__dict__)
