from fastapi import FastAPI

app = FastAPI()

from .tests import tests_router
app.include_router(tests_router)
