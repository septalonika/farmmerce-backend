from fastapi import APIRouter, Depends
from app.views.user import UserView
from app.schemas.user_schema import UserCreate, UserUpdate, PasswordUpdate
from sqlalchemy.orm import Session
from app.instances.db_config import get_db

user_router = APIRouter(prefix="/identity/v1/users", tags=["users"])
user_view = UserView()

@user_router.get("")
async def get_all_users(db: Session = Depends(get_db)):
    return user_view.get_all_users(db)

@user_router.get("/{credential}")
async def get_user(credential, db: Session = Depends(get_db)):
    return user_view.get_user(credential, db)

@user_router.put("/{id}")
async def update_user(id, payload: UserUpdate, db: Session = Depends(get_db)):
    return user_view.update_user(id, payload, db)

@user_router.delete("/{id}")
async def delete_user(id, db: Session = Depends(get_db)):
    return user_view.delete_user(id, db)

@user_router.patch("/{id}")
async def update_password(id: int, payload: PasswordUpdate, db: Session = Depends(get_db)):
    return user_view.update_password(id, payload, db)