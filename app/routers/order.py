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