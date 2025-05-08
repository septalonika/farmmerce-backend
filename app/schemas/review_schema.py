from pydantic import BaseModel, EmailStr
from typing import Optional

class ReviewCreate(BaseModel):
    product_id: int
    review: str
    rating: int
    user_id: int

class ReviewUpdate(BaseModel):
    product_id: Optional[int]
    review: Optional[str]
    rating: Optional[int]
    user_id: Optional[int]