from pydantic import BaseModel
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

class StoreCreate(BaseModel):
    owner_id: int  
    name: str 
    logo: Optional[str] 
    address: str  
    postal_code: int 
    description: str  

