from fastapi import status
from fastapi.responses import JSONResponse
from app.repositories.user import UserRepository
from app.repositories.store import StoreRepository
from sqlalchemy.orm import Session     
from app.views.user import UserView   

class StoreView():
    def __init__(self):
        self.user_repo = UserRepository()
        self.store_repo = StoreRepository()

    def get_store(self, id, db: Session):
        try:
            response = self.store_repo.get_store(id, db)
            if response is None:
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "success": True,
                        "message": "No users found",
                        "status": 404
                    }
                )
            else:
                serialized_response = response.serialize()
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
    
    def get_all_stores(self, db: Session):
        try:
            response = self.store_repo.get_all(db)
            if response is None:
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "success": True,
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
    def create_store(self, payload, db):
        try:
            response = self.store_repo.create_store(payload, db)
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
    def update_store(self, id, payload, db):
        try:
            response = self.store_repo.update_store(id, payload, db)
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
        
    def delete_store(self, id, db):
        try:
            response = self.store_repo.delete_store(id, db)
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