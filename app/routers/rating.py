from fastapi import APIRouter, Depends
from app.views.rating import RatingView
from app.schemas.rating_schema import RatingCreate, RatingUpdate
from sqlalchemy.orm import Session
from app.instances.db_config import get_db

rating_router = APIRouter(prefix="/api/v1/ratings", tags=["ratings"])
rating_view = RatingView()

@rating_router.get("")
async def get_all_rating(db : Session = Depends(get_db)):
    return rating_view.get_all_rating(db)

@rating_router.post("")
async def create_rating(payload: RatingCreate, db : Session = Depends(get_db)):
    return rating_view.create_rating(payload, db)

@rating_router.patch("/{id}")
async def update_rating(id: int, payload: RatingUpdate, db : Session = Depends(get_db)):
    return rating_view.update_rating(id, payload, db)