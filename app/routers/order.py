from fastapi import APIRouter, Depends
from app.views.order import OrderView
from app.schemas.order_schema import OrderCreate, OrderUpdate
from sqlalchemy.orm import Session
from app.instances.db_config import get_db

order_router = APIRouter(prefix="/api/v1/orders", tags=["orders"])
order_view = OrderView()

@order_router.get("")
async def get_all_orders(db: Session = Depends(get_db)):
    return order_view.get_all_orders(db)

@order_router.get("/{id}")
async def get_order(id, db: Session = Depends(get_db)):
    return order_view.get_order(id, db)

@order_router.post("")
async def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    return order_view.create_order(payload, db)

@order_router.put("")
async def update_order(payload: OrderUpdate, db: Session = Depends(get_db)):
    return order_view.update_order(payload, db)
