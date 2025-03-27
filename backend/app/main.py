from fastapi import FastAPI
from .api.router import main_router

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from app.core.di import get_providers


def create_app() -> FastAPI:
    app = FastAPI(
        openapi_url="/core/openapi.json",
        docs_url="/core/docs",
    )
    app.include_router(main_router)
    return app


def main() -> FastAPI:
    # start logging

    app = create_app()
    container = make_async_container(
        *get_providers()
    )
    setup_dishka(container, app)
    return app
