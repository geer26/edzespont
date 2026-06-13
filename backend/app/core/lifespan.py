from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.db import init_db
import logging

_logger = logging.getLogger("app")


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    _logger.info(f"<-------------------- LIFESPAN STARTUP")
    yield
    _logger.info(f"<-------------------- LIFESPAN SHUTDOWN")
