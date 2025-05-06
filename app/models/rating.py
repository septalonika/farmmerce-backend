from app.instances.db_config import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import relationship



class Ratings(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("stores.id"),nullable=False)
    one_star = Column(Integer, nullable=False)
    two_star = Column(Integer, nullable=False)
    three_star = Column(Integer, nullable=False)
    four_star = Column(Integer, nullable=False)
    five_star = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc))
    product = relationship("Products", back_populates="orders")
    
    def __repr__(self):
        return f'<Rating {self.id}>'
    def serialize(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'one_star': self.one_star,
            'two_star': self.two_star,
            'three_star': self.three_star,
            'four_star': self.four_star,
            'five_star': self.five_star,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
    
    def get_id(self):
        return f'{self.id}' 