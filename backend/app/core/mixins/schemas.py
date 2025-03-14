from datetime import datetime
import uuid


class SchemaGETMixin:
    """Миксинка для всех GET схем (scheme)
    Поля соотвествуют полям из app.database.base.DecBase"""
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
