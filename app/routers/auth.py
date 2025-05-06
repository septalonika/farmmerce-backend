from fastapi import APIRouter, Depends
from app.views.auth import AuthView
from app.views.user import UserView
from sqlalchemy.orm import Session
from app.schemas.auth_schema import Login, Register
from app.instances.db_config import get_db
from app.auth.login import require_login, get_current_user_required
from app.models.user import Users

auth_router = APIRouter(prefix="/api/v1/auth", tags=["auth"])
auth_view = AuthView()
user_view = UserView()

@auth_router.post("/login")
async def login(payload: Login, db: Session = Depends(get_db)):
    return auth_view.login(payload, db)

@auth_router.post("register")
async def register(payload: Register, db: Session= Depends(get_db)):
    return user_view.create_user(payload, db)

@auth_router.post("forgot-password")
async def forgot_password():
    pass

@auth_router.get("/me", dependencies=[Depends(require_login)])
async def get_me(current_user: Users = Depends(get_current_user_required)):
    return {"message": "You are authenticated", "username": current_user}
