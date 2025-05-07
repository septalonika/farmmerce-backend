from fastapi import APIRouter, Depends
from app.views.user import UserView
from app.views.store import StoreView
from sqlalchemy.orm import Session
from app.instances.db_config import get_db
from app.schemas.store_schema import StorePayload


store_router = APIRouter(prefix="/api/v1/stores", tags=["users"])
user_view = UserView()
store_view = StoreView()

@store_router.get("")
async def get_all_stores(db: Session = Depends(get_db)):
    return store_view.get_all_stores(db)

@store_router.post("")
async def create_store(payload:StorePayload, db: Session = Depends(get_db)):
    return store_view.create_store(payload, db)

@store_router.put("/{id}")
async def update_store(id, payload, db: Session = Depends(get_db)):
    pass

@store_router.delete("/{id}")
async def delete_store(id, db: Session = Depends(get_db)):
    pass

@store_router.get("/{id}")
async def get_store(id, db: Session = Depends(get_db)):
    pass

