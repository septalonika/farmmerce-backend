from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    email: str

class Login(UserBase):
    email: str
    password: str

class Register(BaseModel):
    email: EmailStr
    username: str
    password: str
    first_name: str
    last_name: str
    gender: Optional[str]
    address: Optional[str]
    postal_code: Optional[int]
    
class Token(BaseModel):
    access_token: str
    token_type: str