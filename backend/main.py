# import uvicorn

# if __name__ == "__main__":
#     uvicorn.run("app.api:app", host="0.0.0.0", port=5001, reload=True)

from fastapi import FastAPI
from app.core.lifespan import lifespan
from app.api import tests_router


app = FastAPI(
    lifespan=lifespan
)

app.include_router(tests_router)
