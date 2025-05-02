"""Initial migration

Revision ID: dafbaa00bbe3
Revises: 5ccd15f04b4e
Create Date: 2025-05-03 00:25:48.407195

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dafbaa00bbe3'
down_revision: Union[str, None] = '5ccd15f04b4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
