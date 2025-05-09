from app.instances.db_config import Base
from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    address = Column(String, nullable=True)
    postal_code = Column(Integer, nullable=True)
    role = Column(Integer, nullable=False, default=1)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(String, nullable=True)
    avatar = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password: str):
        """Hash dan simpan password menggunakan passlib"""
        return pwd_context.hash(password)
        
    def check_password(self, password: str) -> bool:
        """Verifikasi password dengan hash yang tersimpan"""
        return pwd_context.verify(password, self.password)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'gender': self.gender,
            'address': self.address,
            'postal_code': self.postal_code,
            'avatar': self.avatar,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
    
    def get_id(self):
        return f'{self.id}' 