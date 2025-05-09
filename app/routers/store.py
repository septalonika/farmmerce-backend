from fastapi import APIRouter, Depends
from app.views.user import UserView
from app.views.store import StoreView
from sqlalchemy.orm import Session
from app.instances.db_config import get_db
from app.schemas.store_schema import StorePayload, UpdatePayload, StoreCreate


store_router = APIRouter(prefix="/api/v1/stores", tags=["stores"])
user_view = UserView()
store_view = StoreView()

@store_router.get("")
async def get_all_stores(db: Session = Depends(get_db)):
    return store_view.get_all_stores(db)

@store_router.post("")
async def create_store(payload:StoreCreate, db: Session = Depends(get_db)):
    return store_view.create_store(payload, db)

@store_router.put("/{id}")
async def update_store(id, payload:UpdatePayload, db: Session = Depends(get_db)):
    return store_view.update_store(id, payload, db)

@store_router.delete("/{id}")
async def delete_store(id, db: Session = Depends(get_db)):
    return store_view.delete_store(id, db)

@store_router.get("/{id}")
async def get_store(id, db: Session = Depends(get_db)):
    return store_view.get_store(id, db)

