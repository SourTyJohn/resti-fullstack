from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.users import UserRepository
from ..schemas.users import UsersGETSchema, UsersPOSTSchema
from app.core.utils import to_pydantic


class UserService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.user_repo = UserRepository(session)
        
    async def register(self, data: UsersPOSTSchema) -> UsersGETSchema:
        user = await self.user_repo.create(data) # type: ignore
        await self.session.flush()
        return to_pydantic(user, UsersGETSchema)
