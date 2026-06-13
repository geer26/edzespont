from fastapi import APIRouter, Request, Body, Cookie, Header
from app.core.config import SettingsDep
from app.core.db import DbSessionDep
from app.models import User
from sqlmodel import select
from app.services import user_service


tests_router = APIRouter()


@tests_router.get("/", tags=["root"])
async def read_root(settings: SettingsDep) -> dict:
    return {"message": "Welcome to edzespont!", "path": settings.path}


@tests_router.post("/", tags=["root"])
async def write_root() -> dict:
    return {"message": "Write OK!"}


@tests_router.get("/users/")
async def read_all_user(session: DbSessionDep) -> list[User]:
    return user_service.get_all_users(session)
