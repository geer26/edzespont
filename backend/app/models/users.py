import uuid
from datetime import datetime
from sqlalchemy import Boolean, Integer, String, DateTime, ForeignKey, Column
from sqlalchemy.dialects.postgresql import UUID
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    api_key = Column(String, nullable=True)
    fingerprint = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    level = Column(String, nullable=True)
    failed_login_attempt = Column(Integer, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)
