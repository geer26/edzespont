from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.db import create_db_and_tables
import logging

_logger = logging.getLogger("app")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
