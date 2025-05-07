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
            