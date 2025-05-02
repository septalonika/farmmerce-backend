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