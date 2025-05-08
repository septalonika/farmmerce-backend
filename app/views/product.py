from fastapi import status
from fastapi.responses import JSONResponse
from app.repositories.product import ProductRepository
from sqlalchemy.orm import Session

class ProductView():
    def __init__(self):
        self.user_repo = ProductRepository()

    def get_all_products(self, db: Session):
        try:
            response = self.user_repo.get_all(db)
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
        
    def update_product(self, id, payload, db: Session):
        try:
            response = self.user_repo.update_product(id, payload, db)
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
    def delete_product(self, id, db: Session):
        try:
            response = self.user_repo.delete_product(id, db)
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
    def create_product(self, payload, db: Session):
        try:
            response = self.user_repo.create_product(payload, db)
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
    def get_product(self, id, db: Session):
        try:
            response = self.user_repo.get_product(id, db)
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
    def get_product_page(self, page, db: Session):
        try:
            response = self.user_repo.get_product_page(page, db)
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
    def get_product_by_category(self, category, db: Session):
        try:
            response = self.user_repo.get_product_by_category(category, db)
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