from sqlmodel import select, Session as SQLModelSession
from app.core.db import DbSessionDep
from app.models import User
from app.core import password
from app.schemas import user_schema
from uuid import uuid4


def get_all_users(session) -> list[user_schema.UserRead]:
    statement = select(User)
    return session.exec(statement).all()


def get_user_by_id(id: int, session) -> user_schema.UserRead:
    statement = select(User).where(User.id == id)
    return session.exec(statement).one_or_none()


def add_user(user:user_schema.UserCreate, session):
    hashed = password.secure_hash(user.password)
    fingerprint = uuid4().hex
    apikey = password.fast_hash(fingerprint)

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed,
        api_key=apikey,
        fingerprint=fingerprint,
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


def delete_user(id: int, session):
    statement = select(User).where(User.id == id)
    user = session.exec(statement).one_or_none()
    if not user:
        return None
    session.delete(user)
    session.commit()
    remaining = session.exec(select(User)).all()
    return remaining
