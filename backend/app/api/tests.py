from fastapi import APIRouter, Request, Body, Cookie, Header
from app.core.config import SettingsDep
from app.core.db import DbSessionDep
from app.models import User
from app.services import user_service


tests_router = APIRouter()


@tests_router.get("/", tags=["root"])
async def read_root(settings: SettingsDep) -> dict:
    return {"message": "Welcome to edzespont!", "path": settings.path}


@tests_router.post("/", tags=["root"])
async def write_root() -> dict:
    return {"message": "Write OK!"}


