from app.instances.db_config import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from datetime import datetime, timezone
from sqlalchemy.orm import relationship



class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"),nullable=False)
    store_id = Column(Integer, ForeignKey("stores.id"),nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(String, nullable=False, default="pending")
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc))
    
    def __repr__(self):
        return f'<Order {self.id}>'
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'store_id': self.store_id,
            'total_amount': self.total_amount,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
    
    def get_id(self):
        return f'{self.id}' 