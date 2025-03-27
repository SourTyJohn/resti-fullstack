from app.core.dto.users import UserRegisterDTO, UserInDB
from app.database.dao.base import BaseDAO
import uuid

from app.database.models.users import User
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.utils import to_pydantic


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=User, session=session)

    async def get(self, pk: uuid.UUID) -> User | None:
        return await super()._get_by_pk(pk)
    
    async def create(self, data: UserRegisterDTO) -> UserInDB:
        obj = User( **data.model_dump(exclude={"password", } ) )
        self.session.add(obj)
        await self.session.flush()
        return to_pydantic(obj, UserInDB)
