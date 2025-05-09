from pydantic import BaseModel, EmailStr
from typing import Optional

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    rating: int
    image: str
    store_id: int
    created_at: str
    updated_at: str

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    rating: int
    image: Optional[str]
    store_id: int
    weight: int
    category: str

class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    stock: Optional[int]
    rating: Optional[int]
    image: Optional[str]
    