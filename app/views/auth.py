from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from app.repositories.user import UserRepository
from app.models.user import Users
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from app.settings import settings
import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None

class UserInDB(User):
    hashed_password: str

class UsernameInDB:{
    "username": str
}
    
class UserInDB():
    hashed_password: str
    username: str

class Payload():
    email: str
    password: str


class AuthView():
    def __init__(self):
        self.user_repo = UserRepository()
    
    def authenticate_user(self, email: str, password: str, db) -> UsernameInDB | None:
        user : UserInDB = self.user_repo.get_credential(email, db)
        if not user:
            return None
        if not user.check_password(password):
            return None
        return {
            "username": user.username
        }

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return encoded_jwt

    def login(self, payload: Payload, db: Session):
        user = self.authenticate_user(payload.email, payload.password, db)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token_expires = timedelta(days=settings.JWT_REFRESH_TOKEN_EXPIRE_DAYS)
        access_token = self.create_access_token(
            data={"sub": user['username']}, expires_delta=access_token_expires
        )
        refresh_token = self.create_access_token(
            data={"sub": user['username']}, expires_delta=refresh_token_expires
        )
        return JSONResponse({
            "success": True,
            "data": {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "bearer"
            }
        })
    
    def get_me(self, credential, db: Session):
        return self.user_repo.get_user_by(credential, db)
    