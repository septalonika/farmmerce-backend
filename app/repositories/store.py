from app.models.store import Stores
import re


class StoreRepository:
    def get_all(self, db):
        try:
            stores = db.query(Stores).all()
            return stores if stores else None
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None
        
    def create_store(self, payload, db):
        try:
            store = Stores()
            store.name = payload.name
            store.address = payload.address
            store.owner_id = payload.owner_id
            store.description = payload.description

            db.add(store)
            db.commit()
            db.refresh(store)
            return {
                "success": True,
                "data": store.serialize(),
                "message": "Store created successfully",
                "status": 200
            }
        except Exception as e:
            db.rollback()  
            return {
                "success": False,
                "message": str(e),
                "status": 400
            }
        
    def update_store(self, id, payload,db):
        try:
            store = db.query(Stores).filter(Stores.id == id).first()
            store.name = payload.name
            store.address = payload.address
            store.description = payload.description

            db.commit()
            db.refresh(store)
            return {
                "success": True,
                "data": store.serialize(),
                "message": "Store updated successfully",
                "status": 200
            }
        except Exception as e:
            db.rollback()  
            return {
                "success": False,
                "message": str(e),
                "status": 400
            }
    def delete_store(self, id, db):
        try:
            store = db.query(Stores).filter(Stores.id == id).first()
            if store is None:
                return {
                    "success": False,
                    "message": "Store not found",
                    "status": 404
                }
            db.delete(store)
            db.commit()
            return {
                "success": True,
                "message": "Store deleted successfully",
                "status": 200
            }
        except Exception as e:
            db.rollback()
            return {
                "success": False,
                "message": str(e),
                "status": 500
            }