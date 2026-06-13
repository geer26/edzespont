from fastapi import FastAPI
from app.core.lifespan import lifespan
from .tests import tests_router


app = FastAPI(
    lifespan=lifespan
)

app.include_router(tests_router)
