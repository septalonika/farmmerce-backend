from fastapi import APIRouter, Depends
from app.views.user import UserView
from app.schemas.user_schema import UserCreate
from sqlalchemy.orm import Session
from app.instances.db_config import get_db

user_router = APIRouter(prefix="/api/v1/users", tags=["users"])
user_view = UserView()

@user_router.get("")
async def get_all_users(db: Session = Depends(get_db)):
    return user_view.get_all_users(db)

@user_router.get("/{user_id}")
async def get_user_by_id():
    pass

@user_router.post("")
async def create_user(payload: UserCreate):
    return user_view.create_user(payload)

@user_router.put("/{user_id}")
async def update_user():
    pass

@user_router.delete("/{user_id}")
async def delete_user():
    pass