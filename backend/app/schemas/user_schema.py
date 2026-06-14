from sqlmodel import SQLModel
from datetime import datetime


class UserCreate(SQLModel):
    username: str
    email: str
    password: str


class UserRead(SQLModel):
    id: int
    username: str
    email: str
    is_active: bool
    created_at: datetime
    failed_login_attempt: int

class UserUpdate(SQLModel):
    password: str | None = None
    api_key: str | None = None
    failed_login_attempt: int | None = None
    fingerprint: str | None = None
    is_active: bool | None = None