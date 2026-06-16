from fastapi import APIRouter
from app.core.config import SettingsDep
from app.api.enums import Tags


tests_router = APIRouter()


@tests_router.get("/", tags=[Tags.test])
async def read_root(settings: SettingsDep) -> dict:
    return {"message": "Welcome to edzespont!", "path": settings.path}


@tests_router.post("/", tags=[Tags.test])
async def write_root() -> dict:
    return {"message": "Write OK!"}
