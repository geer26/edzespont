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