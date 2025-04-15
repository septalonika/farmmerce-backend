from app.instances.database import metadata
from sqlalchemy import (Table, Column, Integer, Text, JSON, String, Enum, ForeignKey, Time, DateTime)

Sellers_Model = Table(
    'sellers',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50), nullable=False),
    Column('description', Text, nullable=True),
    Column('location', Text, nullable=False),
    Column('type', Enum('organic', 'conventional', name='farm_type'), nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('items', JSON, nullable=True),
) 