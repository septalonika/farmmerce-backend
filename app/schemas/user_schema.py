from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    hashed_password: str
    


class UserCreate(BaseModel):
    email: str
    hashed_password: str


class UserUpdate(BaseModel):
    email: str | None = None
    hashed_password: str | None = None