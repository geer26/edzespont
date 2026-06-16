from app.models import User
from app.core import password
from app.schemas import user_schema
from uuid import uuid4
from sqlalchemy import select

async def get_all_users(session) -> list[user_schema.UserRead]:
    stmt = await session.execute(select(User).order_by(User.created_at.desc()))
    users = stmt.scalars().all()
    return [user_schema.UserRead.model_validate(user) for user in users]

async def get_user_by_id(id, session) -> user_schema.UserRead | None:
    result = await session.execute(select(User).where(User.id == id))
    return result.scalars().one_or_none()

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
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return user_schema.UserRead.model_validate(new_user)

async def delete_user(id, session):
    result = await session.execute(select(User).where(User.id == id))
    user = result.scalars().one_or_none()
    if not user:
        return None
    await session.delete(user)
    await session.commit()
    remaining = await session.execute(select(User))
    return remaining.scalars().all()