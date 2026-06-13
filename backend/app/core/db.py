from sqlmodel import create_engine
from sqlmodel import Session as SQLModelSession
from sqlmodel import SQLModel
from typing import Annotated
from fastapi import Depends

from app.core.config import get_settings

engine = None
SessionLocal = None


def init_db():
    """
    Called during lifespan startup.
    """
    
    global engine, SessionLocal

    settings = get_settings()

    engine = create_engine(
            get_settings().db_connection_string
        )
    
    SQLModel.metadata.create_all(engine)

    engine = create_engine(
        settings.db_connection_string
    )

def get_session():
    with SQLModelSession(engine) as session:
        yield session


DbSessionDep = Annotated[SQLModelSession, Depends(get_session)]
