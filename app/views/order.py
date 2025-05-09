from fastapi import status
from fastapi.responses import JSONResponse
from app.repositories.order import OrderRepository
from sqlalchemy.orm import Session
from app.middleware.s3.rajaOngkir import get_province

class OrderView():
    def __init__(self):
        self.order_repo = OrderRepository()

    def get_order(self, id, db: Session):
        try:
            response = self.order_repo.get_order(id, db)
            if response is None:
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "success": True,
                        "message": "No users found",
                        "status": 404
                    }
                )
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "success": True,
                    "data": response.serialize(),
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
        
    def create_order(self, payload,db: Session):
        try:
            response = self.order_repo.create_order(payload, db)
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
    def update_order_status(self, id, payload, db: Session):
        try:
            response = self.order_repo.update_order_status(id, payload, db)
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
    def get_province(self, keywords):
        try:
            response = get_province(keywords)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "success" : True,
                    "data" : response
                }
            )
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False,
                    "message": str(e)
                }
            )