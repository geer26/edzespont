from sqlmodel import Field, SQLModel
from sqlalchemy import Column, DateTime, func, String
from datetime import datetime


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)

    username: str = Field(
        sa_column=Column(String(50), unique=True, index=True, nullable=False)
    )

    email: str = Field(
        sa_column=Column(String(255), unique=True, index=True, nullable=False)
    )

    password_hash: str = Field(nullable=False)

    is_active: bool = Field(default=True, nullable=False)

    created_at: datetime = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=False),
            server_default=func.now(),
            nullable=False,
        )
    )

    updated_at: datetime = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=False),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )
    )