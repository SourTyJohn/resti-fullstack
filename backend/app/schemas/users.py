from pydantic import BaseModel

from app.core.mixins.schemas import SchemaGETMixin



class UsersPOSTSchema(BaseModel):
    username: str
    password: str


class UsersGETSchema(UsersPOSTSchema, SchemaGETMixin):
    is_superuser: bool


class UsersOnlyUsernameSchema(BaseModel):
    username: str
