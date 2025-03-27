from datetime import datetime
import uuid


class IDMixin:
    id: uuid.UUID


class InDBMixin:
    """Миксинка для всех GET схем (scheme)
    Поля соотвествуют полям из app.database.base.DecBase"""
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
