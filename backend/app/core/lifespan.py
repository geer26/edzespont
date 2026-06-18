from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

_logger = logging.getLogger("app")


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
