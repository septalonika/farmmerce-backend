from app.models.rating import Ratings
import re

class RatingRepository:
    def get_all(self, db):
        try:
            ratings = db.query(Ratings).all()
            return ratings if ratings else None
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None
    def create_rating(self, payload, db):
        try:
            rating = Ratings()
            rating.rating = payload.rating
            rating.product_id = payload.product_id
            rating.user_id = payload.user_id
            db.add(rating)
            db.commit()
            db.refresh(rating)
            return rating.serialize()
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None

    def get_rating(self, id, db):
        try:
            rating = db.query(Ratings).filter(Ratings.id == id).first()
            return rating if rating else None
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None
    
    def update_rating(self, id, payload, db):
        try:
            rating = db.query(Ratings).filter(Ratings.id == id).first()
            rating.rating = payload.rating
            db.commit()
            db.refresh(rating)
            return rating.serialize()
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None
    