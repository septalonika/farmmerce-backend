from app.models.order import Orders
import re

class OrderRepository:

    def get_order(self,id, db):
        try:
            order = db.query(Orders).filter(Orders.id == id).first()
            return order if order else None
        except Exception as e:
            db.rollback()
            print(f"An error Occured: {e}")
            return None
    def get_all(self,db):
        try: 
            orders = db.query(Orders).all()
            return orders if orders else None
        except Exception as e:
            db.rollback()
            print(f"An error Occured: {e}")
            return None
    def create_order(self, payload, db):
        try:
            order = Orders()
            order.total_amount = payload.total_amount
            order.store_id = payload.store_id
            db.add(order)
            db.commit()
            db.refresh(order)
            return order.serialize()
        except Exception as e:
            db.rollback()
            print(f"An error Occured: {e}")
            return None
    
    def update_order_status(self, id, payload, db):
        try: 
            order = db.query(Orders).filter(Orders.id == id).first()
            order.status = payload.status
            db.commit()
            db.refresh(order)
            return order.serialize()

        except Exception as e:
            db.rollback()
            print(f"An error Occured: {e}")
            return None
