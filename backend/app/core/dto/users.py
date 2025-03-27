from pydantic import BaseModel, Field, EmailStr, SecretStr
from app.core.mixins.schemas import InDBMixin


class UserDTO(BaseModel):
    username: str = Field(min_length=4, max_length=16)
    email: EmailStr
    is_superuser: bool = False
    is_active: bool = True


class UserInDB(UserDTO, InDBMixin):
    hashed_password: SecretStr


class UserRegisterDTO(UserDTO):
    password: SecretStr
    hashed_password: SecretStr
