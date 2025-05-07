from app.instances.db_config import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey("stores.id"),nullable=False)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    image = Column(String, nullable=True)
    rating = Column(Integer, nullable=True)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc))
    
    def __repr__(self):
        return f'<Product {self.name}>'
    def serialize(self):
        return {
            'id': self.id,
            'store_id': self.store_id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'description': self.description,
            'rating': self.rating,
            'image': self.image,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
    
    def get_id(self):
        return f'{self.id}' 