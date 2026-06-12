from fastapi import APIRouter, Request, Body, Cookie, Header


tests_router = APIRouter()


@tests_router.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to edzespont!"}


@tests_router.post("/", tags=["root"])
async def write_root() -> dict:
    return {"message": "Write OK!"}
