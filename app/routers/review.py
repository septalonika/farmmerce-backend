from fastapi import APIRouter, Depends
from app.views.review import ReviewView
from app.schemas.review_schema import ReviewCreate, ReviewUpdate
from sqlalchemy.orm import Session
from app.instances.db_config import get_db

review_router = APIRouter(prefix="/api/v1/ratings", tags=["ratings"])
review_view = ReviewView()

@review_router.get("")
async def get_all_reviews(db: Session = Depends(get_db)):
    return review_view.get_all_reviews(db)

@review_router.post("")
async def create_review(payload: ReviewCreate, db: Session = Depends(get_db)):
    return review_view.create_review(db)

@review_router.patch("/{id}")
async def update_review(id: int, payload: ReviewUpdate, db: Session = Depends(get_db)):
    return review_view.update_review(id, payload, db)