from fastapi import APIRouter, Request, Body, Cookie, Header
from app.core.config import SettingsDep
from app.core.db import DbSessionDep
from app.models import User
from app.services import user_service


user_router = APIRouter()


@user_router.get("/users")
async def read_all_user(session: DbSessionDep) -> list[User]:
    return await user_service.get_all_users(session)


@user_router.get("/users/{userid}")
async def gt_user_by_id(userid: int, session: DbSessionDep) -> User:
    return await user_service.get_user_by_id(userid, session)
