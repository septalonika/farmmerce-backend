from datetime import datetime, timezone
from app.models.user import Users
import re
class UserRepository:
    def get_all(self, db):
        try:
            users = db.query(Users).all()
            return users if users else None
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None
    
    def get_credential(self, email, db):
        try:
            users = db.query(Users).filter(Users.email == email).first()
            return users if users else None
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None
        
    def get_user_by(self, credential, db): 
        match credential:
            case int() | str() if str(credential).isdigit():
                credential = int(credential)
                try:
                    user = db.query(Users).filter(Users.id == credential).first()
                    if user is None:
                        return None
                    return user.serialize()
                except:
                    return None
            case _ if "@" in str(credential):
                credential = str(credential)
                try:
                    user = db.query(Users).filter(Users.email == credential).first()
                    if user is None:
                        return None
                    return user.serialize()
                except:
                    return None
            case _:
                try:
                    user = db.query(Users).filter(Users.username == credential).first()
                    if user is None:
                        return None
                    return user.serialize()
                except:
                    return None
        
    def create_user(self,payload, db):
        try:
            user = Users() 
            user.email = payload.email
            user.username = payload.username
            user.first_name = payload.first_name
            user.last_name = payload.last_name
            user.gender = payload.gender
            user.password = user.set_password(payload.password) 
            user.postal_code = payload.postal_code
            if payload.address is not None:
                user.address = payload.address
            if payload.postal_code is not None:
                user.postal_code = payload.postal_code

            db.add(user)
            db.commit()
            db.refresh(user)
            return {
                "success": True,
                "data": user.serialize(),
                "message": "User created successfully",
                "status": 200
            }
        except Exception as e:
            db.rollback()  
            detail_msg = e.orig.diag.message_detail  
            match = re.search(r'Key \((.*?)\)=\((.*?)\)', detail_msg)
            if match:
                    field = match.group(1)      # e.g. 'username'
                    value = match.group(2)      # e.g. 'ur username'
                    message = f"{field} {value} already exists."
            else:
                    message = "Duplicate value violates unique constraint."
            return {
                "success": False,
                "message": message,
                "status": 400
            }
    def update_avatar(self, id, url, db):
        try:
            user = db.query(Users).filter(Users.id == id).first()
            user.avatar = url
            db.commit()
            db.refresh(user)
            return {
                "success": True,
                "data": user.serialize(),
                "message": "Avatar updated successfully",
                "status": 200
            }
        except Exception as e:
            db.rollback()
            return {
                "success": False,
                "message": str(e),
                "status": 500
            }
    def update_user(self, id, payload, db):
        try:
            user = db.query(Users).filter(Users.id == id).first()
            user.email = payload.email
            user.username = payload.username
            user.first_name = payload.first_name
            user.last_name = payload.last_name
            user.gender = payload.gender
            user.updated_at = datetime.now(timezone.utc)
            user.address = payload.address
            user.postal_code = payload.postal_code
            db.commit()
            db.refresh(user)
            return {
                "success": True,
                "data": user.serialize(),
                "message": "User updated successfully",
                "status": 200
            }
        except Exception as e:
            db.rollback()  
            detail_msg = e.orig.diag.message_detail  
            match = re.search(r'Key \((.*?)\)=\((.*?)\)', detail_msg)
            if match:
                    field = match.group(1)      # e.g. 'username'
                    value = match.group(2)      # e.g. 'ur username'
                    message = f"{field} {value} already exists."
            else:
                    message = "Duplicate value violates unique constraint."
            return {
                "success": False,
                "message": message,
                "status": 400
            }
        
    def update_password(self, id, payload, db): 
        try:
            user = db.query(Users).filter(Users.id == id).first()
            user.password = user.set_password(payload.password)
            user.updated_at = datetime.now(timezone.utc)
            db.commit()
            db.refresh(user)
            return {
                "success": True,
                "message": "Password updated successfully",
                "status": 200
            }
        except Exception as e:
            db.rollback()
            return {
                "success": False,
                "message": str(e),
                "status": 500
            }

    def delete_user(self, id, db):
        try:
            user = db.query(Users).filter(Users.id == id).first()
            db.delete(user)
            db.commit()
            return {
                "success": True,
                "message": "User deleted successfully",
                "status": 200
            }
        except Exception as e:
            db.rollback()
            return {
                "success": False,
                "message": str(e),
                "status": 500
            }   