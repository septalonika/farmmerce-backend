from app.instances.database import metadata
from sqlalchemy import (Table, Column, Integer, Text, JSON, String, Enum, ForeignKey, Time, DateTime, LargeBinary)

Products_Model = Table(
    'products',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50), nullable=False),
    Column('description', Text, nullable=True),
    Column('price', String(50), nullable=False),
    Column('quantity', Integer, nullable=False),
    Column('category', String(50), nullable=False),
    Column('seller_id', Integer, ForeignKey('sellers_table.id'), nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('image', LargeBinary, nullable=True)
) 