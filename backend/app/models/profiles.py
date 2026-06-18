import uuid
from datetime import date, datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User


class Profile(SQLModel, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    city: str | None = Field(default=None)
    gender: str | None = Field(default=None)
    avatar_url: str | None = Field(default=None)
    bio: str | None = Field(default=None)
    dob: date | None = Field(default=None)
    height: int | None = Field(default=None)
    weight: int | None = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    user_id: uuid.UUID | None = Field(
        default=None, foreign_key="user.id", unique=True
    )
    user: "User | None" = Relationship(
        back_populates="profile",
        sa_relationship_kwargs={"uselist": False},
    )
