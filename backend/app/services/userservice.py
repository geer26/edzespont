from sqlmodel import select, Session as SQLModelSession
from app.models import User
from fastapi import HTTPException

class UserService:

    async def get_all_users(self, session: SQLModelSession) -> list[User]:
        statement = select(User)
        return session.exec(statement).all()

    async def get_user_by_id(self, id: int, session: SQLModelSession) -> User:
        statement = select(User).where(User.id == id)
        user = session.exec(statement).one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

user_service = UserService()
