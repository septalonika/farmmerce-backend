from fastapi import status
from fastapi.responses import JSONResponse
from app.repositories.user import UserRepository
from sqlalchemy.orm import Session     
from app.views.user import UserView   

class UploadView():
    def __init__(self):
        self.user_repo = UserRepository()
    
    def upload_user_avatar(self, id, url, db):
        try:
            if(UserView().find_user(id, db) is None):
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "success": False,
                        "message": "User not found",
                        "status": 404
                    }
                )
            response = self.user_repo.update_avatar(id, url, db)
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
    def upload_store_avatar(self, id, url, db):
        try:
            if(UserView().find_user(id, db) is None):
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "success": False,
                        "message": "User not found",
                        "status": 404
                    }
                )
            response = self.user_repo.update_avatar(id, url, db)
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
    def add_product_image(self, id, url, db):
        try:
            if(UserView().find_user(id, db) is None):
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "success": False,
                        "message": "User not found",
                        "status": 404
                    }
                )
            response = self.user_repo.update_avatar(id, url, db)
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
            