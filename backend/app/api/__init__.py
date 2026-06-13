from fastapi import FastAPI
from app.core.lifespan import lifespan
from .tests import tests_router
from .user import user_router


app = FastAPI(
    lifespan=lifespan
)

app.include_router(tests_router)
app.include_router(user_router)
