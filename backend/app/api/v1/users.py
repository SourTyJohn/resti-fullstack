from fastapi import APIRouter

from app.core.dto.users import (
    UserRegisterDTO, 
    UserDTO
)

from app.services.users import UserService
from dishka.integrations.fastapi import FromDishka
from dishka.integrations.fastapi import inject


router = APIRouter(
    prefix="/users",
    tags=["Пользователи", ],
)


@inject
async def user_register(
        data: UserRegisterDTO,
        user_service: FromDishka[UserService]
    ) -> UserDTO:
    
    response = await user_service.register(data)
    return response


router.add_api_route(
    '/create',
    user_register,
    response_model=UserDTO,
    methods=['POST', ],
    summary="Новый пользователь"
)
