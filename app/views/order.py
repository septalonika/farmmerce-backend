from fastapi import status
from fastapi.responses import JSONResponse
from app.repositories.order import OrderRepository
from sqlalchemy.orm import Session

class OrderView():
    def __init__(self):
        self.order_repo = OrderRepository()
    
    def get_all_orders(self, db: Session):
        try:
            response = self.order_repo.get_all(db)
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