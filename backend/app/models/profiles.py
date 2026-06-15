from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column, DateTime, func, String
from datetime import datetime
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User  # only imported for type checkers, not at runtime


class Profile(SQLModel, table=True):
    __tablename__ = "profiles"

    id: int | None = Field(default=None, primary_key=True)

    # FK lives on Profile (the "child" side of the 1-to-1)
    user_id: int = Field(foreign_key="users.id", unique=True, index=True, nullable=False)

    first_name: str
    last_name: str
    dob: datetime
    gender: str
    height: int
    weight: int
    avatar_url: str
    bio: str

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

    # one-to-one: profile → user
    user: Optional["User"] = Relationship(back_populates="profile")
