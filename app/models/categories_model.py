from app.instances.database import metadata
from sqlalchemy import (Table, Column, Integer, Text, JSON, String, Enum, ForeignKey, Time, DateTime, LargeBinary)

Categories_Model = Table(
    'categories',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50), nullable=False),
    Column('description', Text, nullable=True),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('image', LargeBinary, nullable=True),
    Column('is_active', Enum('active', 'inactive', name='category_status'), nullable=False, default='active'),
    Column('is_featured', Enum('yes', 'no', name='category_featured'), nullable=False, default='no'),
) 