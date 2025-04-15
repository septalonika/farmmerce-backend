from app.instances.database import metadata
from sqlalchemy import (Table, Column, Integer, Text, JSON, String, Enum, ForeignKey, Time, DateTime, LargeBinary)

Customers_Model = Table(
    'customers',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50), nullable=False),
    Column('description', Text, nullable=True),
    Column('email', String(50), nullable=False, unique=True),
    Column('password', String(255), nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('account_balance', String(50), nullable=False, default='0.00'),
    Column('phone_number', String(20), nullable=True),
    Column('address', Text, nullable=True),
    Column('profile_picture', LargeBinary, nullable=True)
) 