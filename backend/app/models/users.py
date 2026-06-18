from typing import Annotated
import uuid
from sqlmodel import Field, SQLModel
from datetime import datetime



class User(SQLModel, table=True):
    id: uuid.UUID | None = Field(default=uuid.uuid4(), primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(unique=True, index=True)
    password_hash: str | None = Field(default=None)
    api_key: str = Field(index=True)
    fingerprint: str = Field(default=uuid.uuid4())
    is_active: bool = Field(default=True)
    level: str | None = Field(default=None)
    failed_login_attempt: int = Field(default=0)
    created_at: datetime = Field(default=datetime.utcnow())
    updated_at: datetime = Field(default=datetime.utcnow())
