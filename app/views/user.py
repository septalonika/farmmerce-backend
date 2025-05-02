from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from app.repositories.user import UserRepository
from pydantic import BaseModel
from sqlalchemy.orm import Session

class UserCreate(BaseModel):
    username: str
    email: str

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
                print('cugud users', [user.serialize() for user in response])
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
        
    def create_user(self, payload: UserCreate, db):
        try:
            response = self.user_repo.create_user(payload, db)
            return response
        except HTTPException as e:
            raise e 
        except Exception as e:
            raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )
        # try:
        #     return payload
        #     # response = self.user_repo.create()
        # except Exception as e:
        #     return JSONResponse(
        #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         content={
        #             "success": False,
        #             "message": str(e),
        #             "status": 500
        #         }
        #     )
        
        
        # get user from repository
        # if user is None will return response with a error message, success: false and code
        # if user is not None will return response data: user array of dict success: true 201 code
        # resp = []
        # with Session(engine) as session:
        #     self.user_repo = UserRepository(session)
        #     users = self.user_repo.get_all()
        #     if users is None:
        #         resp.append({
        #             "success": False,
        #             "message": "No users found",
        #             "code": 404
        #         })
        #     else:
        #         resp.append({
        #             "success": True,
        #             "data": users,
        #             "code": 200
        #         })

        # @app.get("/users")
# async def get_all_users(db: Session = Depends(get_db)):
#     users = db.query(Users).all()
#     return users


# @app.post('/users')
# async def create_user(
#     data: user_schema.UserCreate,
#     db: Session = Depends(get_db)
# ) -> user_schema.User:
#     user = Users(**data.model_dump())  
#     db.add(user)
#     db.commit()
#     db.refresh(user)

#     user_data = {
#         "id": user.id,
#         "email": user.email,
#         "hashed_password": user.hashed_password
#     }

#     return JSONResponse(
#         status_code=201,
#         content={
#             "data": user_data,
#             "message": "Users Created",
#             "status": 201
#         }
#     )

# @app.get('/users/{user_id}')
# async def read_user(
#     user_id: int,
#     db: Session = Depends(get_db)
# ) -> user_schema.User:
#     user = db.get(Users, user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail='Item not found')
#     return user