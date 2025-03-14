from app.schemas.users import UsersPOSTSchema, UsersGETSchema
from app.core.database import BaseRepository

from app.models.users import User


class UserRepository(BaseRepository):
    model = User

    async def get(self, pk: int) -> User | None:
        return await super().get(pk)
    
    async def create(self, data: UsersPOSTSchema) -> User:
        return await super().create(data)
    
    async def update(self, data: UsersGETSchema) -> User:
        return await super().update(data)
    
    async def delete(self, pk: int) -> None:
        await super().delete(pk)
