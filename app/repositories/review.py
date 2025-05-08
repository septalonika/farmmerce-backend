from app.models.review import Reviews
import re

class ReviewRepository:
    def get_all(self, db):
        try:
            reviews = db.query(Reviews).all()
            return reviews if reviews else None
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None
        
    def get_review(self, id, db):
        try:
            review = db.query(Reviews).filter(Reviews.id == id).first()
            return review if review else None
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None
        
    def create_review(self, product_id, payload, db):
        try:
            review = Reviews()
            review.review = payload.review
            review.product_id = product_id
            db.add(review)
            db.commit()
            db.refresh(review)
            return review.serialize()
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None
    
    def update_review(self, id, payload, db):
        try:
            review = db.query(Reviews).filter(Reviews.id == id).first()
            review.review = payload.review
            db.commit()
            db.refresh(review)
            return review.serialize()
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None
    