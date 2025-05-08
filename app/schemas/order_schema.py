from pydantic import BaseModel, EmailStr
from typing import Optional

class Order(BaseModel):
    id: int
    user_id: int
    store_id: int
    total_amount: float
    status: str

class OrderCreate(BaseModel):
    user_id: int
    store_id: int
    total_amount: float
    status: Optional[str]

class OrderUpdate(BaseModel):
    user_id: Optional[int]
    store_id: Optional[int]
    total_amount: Optional[float]
    status: Optional[str]

