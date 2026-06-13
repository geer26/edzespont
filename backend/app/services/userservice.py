from sqlmodel import select, Session as SQLModelSession
from app.models import User

class UserService:
    def get_all_users(self, session: SQLModelSession) -> list[User]:
        statement = select(User)
        return session.exec(statement).all()

user_service = UserService()
