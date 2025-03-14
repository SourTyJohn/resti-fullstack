from fastapi import APIRouter
from .v1 import users


api_v1_router = APIRouter(
    prefix='/v1',
    tags=['v1', ]
)


api_v1_router.include_router(users.router)
# include routers here
