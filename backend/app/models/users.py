import uuid
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .profiles import Profile

class User(SQLModel, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(unique=True, index=True)
    password_hash: str | None = Field(default=None)
    api_key: str = Field(index=True)
    fingerprint: uuid.UUID = Field(default_factory=uuid.uuid4)
    is_active: bool = Field(default=True)
    level: str | None = Field(default=None)
    failed_login_attempt: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    profile: "Profile | None" = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"uselist": False},
    )