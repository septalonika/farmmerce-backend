from fastapi import HTTPException, status
from app.models.user import Users
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
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
        
    def get_user(self, id, db):
        pass 
        
    def create_user(self,payload, db):
        try:
            user = Users() 
            user.email = payload.email
            user.username = payload.username
            user.first_name = payload.first_name
            user.last_name = payload.last_name
            user.gender = payload.gender
            user.password = user.set_password(payload.password) 

            db.add(user)
            db.commit()
            db.refresh(user)
            return user.serialize()
        except IntegrityError as e:
            db.rollback()  
            if isinstance(e.orig, UniqueViolation):
                detail_msg = e.orig.diag.message_detail  
                match = re.search(r'Key \((.*?)\)=\((.*?)\)', detail_msg)
                if match:
                        field = match.group(1)      # e.g. 'username'
                        value = match.group(2)      # e.g. 'ur username'
                        message = f"{field} {value} already exists."
                else:
                        # Fallback message if regex fails
                        message = "Duplicate value violates unique constraint."
                    
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=message
                )
            else:
                raise