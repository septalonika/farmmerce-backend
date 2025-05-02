from app.instances.db_config import database
from fastapi import FastAPI
from app.routers.user import user_router
from app.settings import settings
from contextlib import asynccontextmanager
from app.views.user import UserView
import os
from dotenv import load_dotenv

# Load .env file - this should be at the very beginning of your application
load_dotenv(override=True)


def create_app():

    print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")
    app = FastAPI()
    @app.get("/")
    def read_root():
        return {"Message": "This is Index of Farmmerce API"}

    app.include_router(user_router)

    return app

app = create_app()