from app.models.order import Orders
import re

class OrderRepository:

    def get_all(self,db):
        try: 
            users = db.query(Orders).all()
            return users if users else None
        except Exception as e:
            db.rollback()
            print(f"An error Occured: {e}")
    