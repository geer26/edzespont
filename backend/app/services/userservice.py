from app.models import User
from fastapi import HTTPException
from app.repositories import user_repository as user_repo
from app.schemas import user_schema

class UserService():

    async def get_all_users(self, session) -> list[user_schema.UserRead]:
        users = user_repo.get_all_users(session)
        return [user_schema.UserRead.model_validate(u) for u in users]

    async def get_user_by_id(self, id: int, session) -> user_schema.UserRead:
        user = user_repo.get_user_by_id(id, session)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user_schema.UserRead.model_validate(user)

    async def add_user(self, user: user_schema.UserCreate, session):
        new_user = user_repo.add_user(user, session)
        return user_schema.UserRead.model_validate(new_user)

user_service = UserService()
