# import uuid
# from datetime import datetime, date
# from sqlalchemy import Integer, String, Text, DateTime, ForeignKey, Column
# from sqlalchemy.dialects.postgresql import UUID
# from .base import Base



# class Profile(Base):
#     __tablename__ = "profiles"

#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

#     first_name = Column(String, nullable=True)
#     last_name = Column(String, nullable=True)
#     gender = Column(String, nullable=True)
#     avatar_url = Column(String, nullable=True)
#     bio = Column(Text, nullable=True)
#     dob = Column(DateTime, nullable=True)
#     height = Column(Integer, nullable=True)
#     weight = Column(Integer, nullable=True)

#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime)


    # FK lives on Profile (the "child" side of the 1-to-1)
    # user_id: int = Field(foreign_key="users.id", unique=True, index=True, nullable=False)
    # one-to-one: profile → user
    # user: Optional["User"] = Relationship(back_populates="profile")


from typing import Annotated
import uuid
from sqlmodel import Field, SQLModel
from datetime import datetime, date


class Profile(SQLModel, table=True):
    id: uuid.UUID | None = Field(default=uuid.uuid4(), primary_key=True)
    first_name: str = Field()
    last_name: str = Field()
    gender: str = Field()
    avatar_url: str = Field()
    bio: str = Field()
    dob: date = Field()
    height: int = Field()
    weight: int = Field()
    created_at: datetime = Field(default=datetime.utcnow())
    updated_at: datetime = Field(default=datetime.utcnow())
