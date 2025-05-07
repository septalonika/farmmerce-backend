from app.instances.db_config import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Stores(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"),nullable=False)
    name = Column(String, nullable=False)
    logo = Column(String, nullable=True)
    description = Column(String, nullable=False)    
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc))
    
    def __repr__(self):
        return f'<Store {self.name}>'
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'owner_id': self.owner_id,
            'logo': self.logo,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
    
    def get_id(self):
        return f'{self.id}' 