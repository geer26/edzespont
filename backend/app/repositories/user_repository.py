from http import HTTPMethod
from fastapi import HTTPException, status
from app.models import User
from app.core import password
from app.schemas import user_schema
from uuid import uuid4
from sqlmodel import select


async def get_all_users(session) -> list[user_schema.UserRead]:
    users = session.exec(select(User)).all()
    return [user_schema.UserRead.model_validate(user) for user in users]

async def get_user_by_id(id, session) -> user_schema.UserRead | None:
    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")
    return user

async def add_user(user: user_schema.UserCreate, session):
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
    try:
        session.add(new_user)
        session.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    session.refresh(new_user)
    return user_schema.UserRead.model_validate(new_user)

async def delete_user(id, session):
    user = session.get(User, id)
    if not user:
        return None
    try:
        session.delete(user)
        session.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    users = session.exec(select(User)).all()
    return [user_schema.UserRead.model_validate(user) for user in users]
