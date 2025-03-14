from fastapi import FastAPI

from .api.router import api_v1_router


app = FastAPI(
    openapi_url="/core/openapi.json",
    docs_url="/docs",
)
app.include_router(api_v1_router)
