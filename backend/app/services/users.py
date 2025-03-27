from sqlalchemy.ext.asyncio import AsyncSession

from app.database.dao.users import UserDAO
from app.core.dto.users import UserRegisterDTO, UserDTO, UserInDB
from app.core.utils import to_pydantic
from app.core.security import get_password_hash


__all__ = (
    "UserService",
)


class UserService:
    def __init__(self,
                session: AsyncSession,
                user_dao: UserDAO
        ) -> None:

        self.session = session
        self.user_dao = user_dao

    async def register(self, data: UserRegisterDTO) -> UserDTO:
        password = data.password.get_secret_value()
        data.hashed_password = get_password_hash(password) # type: ignore

        user: UserInDB = await self.user_dao.create(data)
        await self.session.commit()
        return user
 