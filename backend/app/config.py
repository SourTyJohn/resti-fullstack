from datetime import timezone, timedelta
from functools import lru_cache
from pathlib import Path
import os

from dotenv import get_key


BASE_PATH = Path(__file__).parent.parent.parent 


class Settings:
    DEFAULT_ENV_FILE  = BASE_PATH / '.env.dev'

    def __init__(self):
        self.__env_file = Settings.DEFAULT_ENV_FILE

        self.TIMEZONE: timezone | None = timezone(
            timedelta(
                hours=int(self.__get_env("TZ")[-2:])  # type: ignore
        ))
        self.ENVIRONMENT:                    str | None = self.__get_env("ENVIRONMENT")
        self.STACK_NAME:                     str | None = self.__get_env("STACK_NAME")
        self.INNER_HOST:                     str | None = self.__get_env("INNER_HOST")
        self.DB_FIRST_SUPERUSER:             str | None = self.__get_env("DB_FIRST_SUPERUSER")
        self.DB_URI:                         str | None = self.__get_env("DB_URI")
    
        self.DB_FIRST_SUPERUSER_PASSWORD: str | None = self.__get_env(
            "DB_FIRST_SUPERUSER_PASSWORD",
            required=False
        )
        if self.DB_FIRST_SUPERUSER_PASSWORD is None:
            file_path = self.__get_env("DB_FIRST_SUPERUSER_PASSWORD_FILE")
            with open(file_path) as file:  # type: ignore
                self.DB_FIRST_SUPERUSER_PASSWORD = file.read().strip()

        self.DB_PASSWORD: str | None = self.__get_env(
            "DB_PASSWORD",
            required=False
        )
        if self.DB_PASSWORD is None:
            file_path = self.__get_env("DB_PASSWORD_FILE")
            with open(file_path) as file:
                self.DB_PASSWORD = file.read().strip()

        self.SECRET_KEY: str | None = self.__get_env(
            "SECRET_KEY",
            required=False
        )
        if self.SECRET_KEY is None:
            file_path = self.__get_env("SECRET_KEY_FILE")
            with open(file_path) as file:
                self.SECRET_KEY = file.read().strip()

        self.DB_URI = self.DB_URI.replace("%PATH%", str(BASE_PATH / "backend")) # type: ignore
        self.DB_URI = self.DB_URI.replace("%DB_PASSWORD%", self.DB_PASSWORD) # type: ignore

    def __get_env(
            self,
            env_variable: str,
            required: bool = True
        ) -> str | None:

        value = ''
        if self.__env_file is not None and os.path.exists(self.__env_file):
            value = get_key(self.__env_file, env_variable)
        if value is None or len(value) == 0:
            try:
                value = os.environ[env_variable]
            except KeyError:
                if not required:
                    return None
                
                raise KeyError(f"Required settings variable not found: {env_variable}")

        return value


@lru_cache()
def config() -> Settings:
    return Settings()
