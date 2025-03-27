from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from typing import AsyncIterable

from app.services.users import UserService
from app.database.dao.users import UserDAO


class ServicesProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def get_user_service(
            self, session: AsyncSession, user_dao: UserDAO
        ) -> AsyncIterable[UserService]:
        service = UserService(session, user_dao)
        print("Работаем с сервисом")
        yield service
        print("Отпустили")
