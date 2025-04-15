from app.instances.database import metadata
from sqlalchemy import (Table, Column, Integer, Text, JSON, String, Enum, ForeignKey, Time, DateTime, LargeBinary)

Admins_Model = Table(
    'admins',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50), nullable=False),
    Column('description', Text, nullable=True),
    Column('email', String(50), nullable=False, unique=True),
    Column('password', String(255), nullable=False),
    Column('role', Integer, nullable=False, default=1),  # 1 for admin, 2 for super admin
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    Column('phone_number', String(20), nullable=True),
    Column('address', Text, nullable=True),
    Column('profile_picture', LargeBinary, nullable=True),
) 