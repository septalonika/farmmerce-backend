from instances.db_config import Base
from sqlalchemy import Column, Integer, String

class Users(Base):
    __tablename__ = "users"

    id = Base.Column(Integer, primary_key=True, index=True)
    email = Base.Column(String, unique=True, index=True)
    hashed_password = Base.Column(String)
