from sqlmodel import Field, SQLModel
from datetime import date


class ProfileUpdate(SQLModel):
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    gender: str | None = Field(default=None)
    avatar_url: str | None = Field(default=None)
    bio: str | None = Field(default=None)
    dob: date | None = Field(default=None)
    height: int | None = Field(default=None)
    weight: int | None = Field(default=None)