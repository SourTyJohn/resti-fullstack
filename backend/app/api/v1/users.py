from fastapi import APIRouter

from app.schemas.users import (
    UsersPOSTSchema,
    UsersGETSchema,
)
from app.services.users import UserService

from app.api.deps import SessionDep
from app.core.database import transaction


router = APIRouter(
    prefix="/users",
    tags=["Пользователи", ],
)


@router.post('/create', summary="Новый пользователь")
async def user_register(data: UsersPOSTSchema, session: SessionDep) -> UsersGETSchema:
    user_service = UserService(session)
    async with transaction(session):
        response = await user_service.register(data) # type: ignore
    return response
