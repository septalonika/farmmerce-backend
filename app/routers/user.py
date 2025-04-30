from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.views.user import UserView
# from app.dependencies import get_db, get_current_user
# from app.views.user import UserView

user_router = APIRouter(prefix="/api/v1/users", tags=["users"])
user_view = UserView()

@user_router.get("")
async def get_all_users():
    return user_view.get_all_users()

@user_router.get("/{user_id}")
async def get_user_by_id():
    pass

@user_router.post("")
async def create_user():
    pass

@user_router.put("/{user_id}")
async def update_user():
    pass

@user_router.delete("/{user_id}")
async def delete_user():
    pass