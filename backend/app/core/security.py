from datetime import datetime, timedelta, timezone
from typing import Any, Union

import jwt
from passlib.context import CryptContext

from app.config import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"
DEFAULT_TIMEDELTA_FOR_ACCESSTOKEN = timedelta(days=1)


def create_access_token(
        subject: str | Any, expires_delta: timedelta | None = None
        ) -> str:
    if expires_delta is None:
        expires_delta = DEFAULT_TIMEDELTA_FOR_ACCESSTOKEN

    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = { "exp": expire, "sub": str(subject) }
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
