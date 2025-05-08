from pydantic import BaseModel, EmailStr
from typing import Optional 

class RatingCreate(BaseModel):
    product_id: int
    rating: int

class RatingUpdate(BaseModel):
    product_id: Optional[int]
    rating: Optional[int]