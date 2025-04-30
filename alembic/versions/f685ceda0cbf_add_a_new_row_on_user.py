"""add a new row on user

Revision ID: f685ceda0cbf
Revises: db8c0be39ba7
Create Date: 2025-04-30 18:21:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f685ceda0cbf'
down_revision = 'db8c0be39ba7'
branch_labels = None
depends_on = None

gender_enum = postgresql.ENUM('Male', 'Female', name='gender')

def upgrade():
    gender_enum.create(op.get_bind(), checkfirst=True)
    op.add_column('users', sa.Column('gender', gender_enum, nullable=True))

def downgrade():
    op.drop_column('users', 'gender')
    gender_enum.drop(op.get_bind(), checkfirst=True)
