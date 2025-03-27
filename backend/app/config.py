from datetime import timezone, timedelta
from functools import cache
import os

from dotenv import get_key

try:
    ENV_FILE_PATH = os.environ["PATH_TO_BACKEND_DOTENV_FILE"]
except KeyError:
    print("environment variable PATH_TO_BACKEND_DOTENV_FILE not set")
    ENV_FILE_PATH = None


class Settings:
    def __init__(self):
        self.__env_file = ENV_FILE_PATH

        self.TIMEZONE: timezone = timezone(
            timedelta(
                hours=int(self.__get_env_req("TZ")[-2:])  # type: ignore
        ))
        self.ENVIRONMENT:          str = self.__get_env_req("ENVIRONMENT")
        self.STACK_NAME:           str = self.__get_env_req("STACK_NAME")
        self.INNER_HOST:           str = self.__get_env_req("INNER_HOST")
        self.DB_FIRST_SUPERUSER:   str = self.__get_env_req("DB_FIRST_SUPERUSER")
        self.DB_URI:               str = self.__get_env_req("DB_URI")
    
        self.DB_FIRST_SUPERUSER_PASSWORD: str = self.__get_env(
            "DB_FIRST_SUPERUSER_PASSWORD",
            required=False
        )  # type: ignore
        if self.DB_FIRST_SUPERUSER_PASSWORD is None:
            file_path = self.__get_env_req("DB_FIRST_SUPERUSER_PASSWORD_FILE")
            with open(file_path) as file:
                self.DB_FIRST_SUPERUSER_PASSWORD = file.read().strip()

        self.DB_PASSWORD: str = self.__get_env(
            "DB_PASSWORD",
            required=False
        ) # type: ignore
        if self.DB_PASSWORD is None:
            file_path = self.__get_env_req("DB_PASSWORD_FILE")
            with open(file_path) as file:
                self.DB_PASSWORD = file.read().strip()

        self.SECRET_KEY: str = self.__get_env(
            "SECRET_KEY",
            required=False
        ) # type: ignore
        if self.SECRET_KEY is None:
            file_path = self.__get_env_req("SECRET_KEY_FILE")
            with open(file_path) as file:
                self.SECRET_KEY = file.read().strip()

        self.DB_URI = self.DB_URI.replace("%DB_PASSWORD%", self.DB_PASSWORD) # type: ignore

    def __get_env_req(self, env_variable: str) -> str:
        r = self.__get_env(env_variable=env_variable)
        if r is not None:
            return r
        raise ValueError()
    
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


def config() -> Settings:
    __cfg = Settings()
    return __cfg
