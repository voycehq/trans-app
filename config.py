import os
import sys
from functools import lru_cache
from pydantic import BaseSettings, Field

base_dir = os.path.abspath(sys.path[0])


class FactoryConfig(BaseSettings):
    PORT: str
    ENV: str = Field(..., env='ENV')
    SQLALCHEMY_DATABASE_URL: str
    TRANSLATOR_URL: str

    class Config:
        env_file = os.path.join(base_dir, '.env')


@lru_cache()
def settings():
    return FactoryConfig()


config = settings()
