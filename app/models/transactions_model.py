from app.instances.database import metadata
from sqlalchemy import (Table, Column, Integer, Text, JSON, String, Enum, ForeignKey, Time, DateTime)

Transactions_Model = Table(
    'transactions',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('amount', String(50), nullable=False),
    Column('transaction_type', Enum('credit', 'debit', name='transaction_type'), nullable=False),
    Column('customer_id', Integer, ForeignKey('customers_table.id'), nullable=False),
    Column('seller_id', Integer, ForeignKey('sellers_table.id'), nullable=False),
    Column('description', Text, nullable=True),
    Column('created_at', DateTime, nullable=False),
) 