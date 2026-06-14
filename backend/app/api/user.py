from fastapi import APIRouter, Request, Body, Cookie, Header, status
from app.core.db import DbSessionDep
from app.schemas import user_schema
from app.services import user_service


user_router = APIRouter()


@user_router.get("/users", response_model=list[user_schema.UserRead])
async def read_all_user(session: DbSessionDep):
    return await user_service.get_all_users(session)


@user_router.get("/users/{userid}", response_model=user_schema.UserRead)
async def get_user_by_id(userid: int, session: DbSessionDep):
    return await user_service.get_user_by_id(userid, session)


@user_router.post("/users", response_model=list[user_schema.UserRead], status_code=status.HTTP_201_CREATED)
async def add_user(user: user_schema.UserCreate, session: DbSessionDep):
    return await user_service.add_user(user, session)


@user_router.delete("/users/{userid}", response_model=list[user_schema.UserRead])
async def delete_user(userid: int, session: DbSessionDep):
    return await user_service.delete_user(userid, session)
