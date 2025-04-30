from sqlalchemy.orm import Session
from app.models.user import Users
from app.instances.db_config import get_db

class UserRepository:
    def get_all(self):
        db = next(get_db())
        try:
            users = db.query(Users).all()
            return users if users else None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None