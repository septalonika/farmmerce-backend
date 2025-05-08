from app.instances.db_config import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import relationship

class Reviews(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"),nullable=False)
    product_id = Column(Integer, ForeignKey("stores.id"),nullable=False)
    rating_id = Column(Integer, ForeignKey("ratings.id"),nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc))
    
    def __repr__(self):
        return f'<Review {self.id}>'
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
    
    def get_id(self):
        return f'{self.id}' 