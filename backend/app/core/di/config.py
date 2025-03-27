from dishka import Provider, Scope, provide
from app.config import config, Settings


class ConfigProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_config(self) -> Settings:
        return config()
