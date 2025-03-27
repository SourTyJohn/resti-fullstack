from .config import ConfigProvider
from .database import DatabaseProvider
from .service import ServicesProvider
from .dao import DaoProvider


def get_providers():
    return [
        ConfigProvider(),
        DatabaseProvider(),
        ServicesProvider(),
        DaoProvider()
    ]
