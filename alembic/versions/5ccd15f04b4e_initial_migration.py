"""Initial migration

Revision ID: 5ccd15f04b4e
Revises: ca4f21c313f2
Create Date: 2025-05-03 00:25:13.704163

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ccd15f04b4e'
down_revision: Union[str, None] = 'ca4f21c313f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
