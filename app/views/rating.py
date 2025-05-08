from fastapi import status
from fastapi.responses import JSONResponse
from app.repositories.rating import RatingRepository
from sqlalchemy.orm import Session

class RatingView:
    def __init__(self):
        self.rating_repo = RatingRepository()

    def get_all_rating(self, db: Session):
        try:
            response = self.rating_repo.get_all(db)
            if response is None:
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "success": True,
                        "message": "No Ratings found",
                        "status": 404
                    }
                )
            else:
                serialized_response = [rating.serialize() for rating in response]
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