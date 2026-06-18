from fastapi import FastAPI
# from app.core.lifespan import lifespan
from .tests import tests_router
from .user import user_router
from ..core.smdb import create_db_and_tables


app = FastAPI(
    # lifespan=lifespan
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(tests_router)
app.include_router(user_router)
