from app.models.user import Users
from app.instances.db_config import get_db
from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.schemas import user_schema
from fastapi.responses import JSONResponse
from app.routers.user import user_router

def create_app():
    app = FastAPI()
    
    @app.get("/")
    def read_root():
        return {"message": "this is index of app"}

    app.include_router(user_router)
    return app

# Create the FastAPI app instance
app = create_app()