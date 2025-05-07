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
            # detail_msg = 
            # match = re.search(r'Key \((.*?)\)=\((.*?)\)', detail_msg)
            # if match:
            #         field = match.group(1)      # e.g. 'username'
            #         value = match.group(2)      # e.g. 'ur username'
            #         message = f"{field} {value} already exists."
            # else:
            #         message = "Duplicate value violates unique constraint."
            return {
                "success": False,
                "message": str(e),
                "status": 400
            }