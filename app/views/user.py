from fastapi import status
from fastapi.responses import JSONResponse
from app.repositories.user import UserRepository
from sqlalchemy.orm import Session

class UserView():
    def __init__(self):
        self.user_repo = UserRepository()
    
    def get_all_users(self, db: Session):
        try:
            response = self.user_repo.get_all(db)
            if response is None:
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "success": False,
                        "message": "No users found",
                        "status": 404
                    }
                )
            else:
                serialized_response = [user.serialize() for user in response]
                return JSONResponse(
                    status_code=status.HTTP_200_OK,
                    content={
                        "success": True,
                        "data": serialized_response,
                        "status": 200
                    }
                )
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "success": False,
                    "message": str(e),
                    "status": 500
                }
            )
        
    def find_user(self, credential, db: Session):
        user = self.user_repo.get_user_by(credential, db)
        return user
    
    def get_user(self, credential, db: Session):
        try:
            user = self.find_user(credential, db)
            if(user is None):
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "success": False,
                        "message": "User not found",
                        "status": 404
                    }
                )
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "success": True,
                    "data": user,
                    "status": 200
                }
            )
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "success": False,
                    "message": str(e),
                    "status": 500
                }
            )
        
    
    def create_user(self, payload, db):
        try:
            response = self.user_repo.create_user(payload, db)
            if(response['success'] == False):
                return JSONResponse(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    content={
                        "success": False,
                        "message": response['message'],
                        "status": 500
                    }
                )
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "success": True,
                    "data": response,
                    "message": response['message'],
                    "status": 200
                }
            )
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "success": False,
                    "message": str(e),
                    "status": 500
                }
            )
    def update_user(self, id, payload, db):
        try:
            if(self.find_user(id, db) is None):
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "success": False,
                        "message": "User not found",
                        "status": 404
                    }
                )
            response = self.user_repo.update_user(id, payload, db)
            if(response['success'] == False):
                return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                        "success": False,
                        "message": response['message'],
                        "status": 500
                    }
                )
            return JSONResponse(
                    status_code=status.HTTP_200_OK,
                    content={
                        "success": True,
                        "data": response,
                        "message": response['message'],
                        "status": 200
                    }
                )
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "success": False,
                    "message": str(e),
                    "status": 500
                }
            )
    
    def update_password(self, id, payload, db):
        try:
            if(self.find_user(id, db) is None):
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "success": False,
                        "message": "User not found",
                        "status": 404
                    }
                )
            response = self.user_repo.update_password(id, payload, db)
            if(response['success'] == False):
                return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                        "success": False,
                        "message": response['message'],
                        "status": 500
                    }
                )
            return JSONResponse(
                    status_code=status.HTTP_200_OK,
                    content={
                        "success": True,
                        "data": response,
                        "message": response['message'],
                        "status": 200
                    }
                )
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "success": False,
                    "message": str(e),
                    "status": 500
                    }
            )
        
    def delete_user(self, id, db):
        try:
            if(self.find_user(id, db) is None):
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "success": False,
                        "message": "User not found",
                        "status": 404
                    }
                )
            response = self.user_repo.delete_user(id, db)
            if(response['success'] == False):
                return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                        "success": False,
                        "message": response['message'],
                        "status": 500
                    }
                )
            return JSONResponse(
                    status_code=status.HTTP_200_OK,
                    content={
                        "success": True,
                        "data": response,
                        "message": response['message'],
                        "status": 200
                    }
                )
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "success": False,
                    "message": str(e),
                    "status": 500
                }
            )   