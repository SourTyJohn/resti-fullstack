from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.dao.users import UserDAO


class DaoProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def get_user_dao(self, session: AsyncSession) -> UserDAO:
        return UserDAO(session)
