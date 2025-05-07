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
        pass
            