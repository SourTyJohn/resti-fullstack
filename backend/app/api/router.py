from fastapi import APIRouter
from .v1 import users as v1_users
from app.api.utils import utils_router

main_router = APIRouter(
    prefix='/api'
)

# UTILS
main_router.include_router(utils_router)
# --


# API v1
api_v1_router = APIRouter(
    prefix='/v1',
    tags=['v1', ]
)
api_v1_router.include_router(v1_users.router)
# ...

main_router.include_router(api_v1_router)
# --
