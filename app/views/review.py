from fastapi import status
from fastapi.responses import JSONResponse
from app.repositories.review import ReviewRepository
from sqlalchemy.orm import Session

class ReviewView:
    def __init__(self):
        self.review_repo = ReviewRepository()
    
    def get_all_reviews(self,db):
        try:
            response = self.review_repo.get_all(db)
            if response is None:
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "success": True,
                        "message": "No Reviews found",
                        "status": 404
                    }
                )
            else:
                serialized_response = [review.serialize() for review in response]
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
    