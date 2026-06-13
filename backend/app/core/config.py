import os
from typing import Annotated
from fastapi import Depends
from functools import lru_cache


class Settings():

    def __init__(self):
        self.db_connection_string = os.getenv("DB_CONNECTION_STRING") \
        or "postgresql+psycopg2://geer26:726354Valami01?@edzespont_db:5432/edzespont"
        self.path = os.getcwd()


@lru_cache
def get_settings():
    return Settings()


SettingsDep =  Annotated[Settings, Depends(get_settings)]
