from pydantic import BaseModel, EmailStr
from typing import Optional

class StorePayload(BaseModel):
    name: str
    address: str
    description: str
    owner_id: int

class UpdatePayload(BaseModel):
    name: str
    address: str
    description: str
