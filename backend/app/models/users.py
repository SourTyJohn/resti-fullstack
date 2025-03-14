from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import DecBase


class User(DecBase):
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    is_superuser: Mapped[bool] = mapped_column(default=False)
