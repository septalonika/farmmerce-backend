from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum
class User(BaseModel):
    id: int
    email: str
    password: str

class GenderEnum(str, Enum):
    Male = "Male"
    Female = "Female"

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    first_name: str
    last_name: str
    gender: Optional[GenderEnum]

class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[GenderEnum]

class PasswordUpdate(BaseModel):
    password: str