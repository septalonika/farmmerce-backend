from functools import lru_cache
import os 
import logging

from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    APP_NAME: str
    ORIGINS: list
    CORS_ALLOW_METHODS: list
    CORS_ALLOW_HEADERS: list

    class Config:
        env_file = os.environ.get("ENV_FILE", ".env")
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings() -> Settings:
    """
    Get the settings from the environment variables.
    """
    return Settings()

settings = get_settings()