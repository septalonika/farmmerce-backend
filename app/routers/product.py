from fastapi import APIRouter, Depends
from app.views.product import ProductView
from app.schemas.product_schema import ProductCreate, ProductUpdate
from sqlalchemy.orm import Session
from app.instances.db_config import get_db

product_router = APIRouter(prefix="/api/v1/products", tags=["products"])
product_view = ProductView()

@product_router.get("")
async def get_all_products(db: Session = Depends(get_db)):
    return product_view.get_all_products(db)

@product_router.put("/{id}")
async def update_product(id, payload: ProductUpdate, db: Session = Depends(get_db)):
    return product_view.update_product(id, payload, db)

@product_router.delete("/{id}")
async def delete_product(id, db: Session = Depends(get_db)):
    return product_view.delete_product(id, db)

@product_router.post("")
async def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    return product_view.create_product(payload, db)

@product_router.get("/{id}")
async def get_product(id, db: Session = Depends(get_db)):
    return product_view.get_product(id, db)

# create pagination for product
@product_router.get("/page/{page}")
async def get_product_page(page, db: Session = Depends(get_db)):
    return product_view.get_product_page(page, db)  

@product_router.get("/category/{category}")
async def get_product_by_category(category, db: Session = Depends(get_db)):
    return product_view.get_product_by_category(category, db)



