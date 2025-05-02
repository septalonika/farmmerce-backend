from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# Revision identifiers, used by Alembic.
revision: str = '288dcbd55acc'
down_revision: Union[str, None] = 'dafbaa00bbe3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Add the password column
    op.add_column('users', sa.Column('password', sa.String(), nullable=False, server_default=''))
    op.alter_column('users', 'password', server_default=None)

    # Create the gender enum type
    gender_enum = postgresql.ENUM('Male', 'Female', name='gender')
    gender_enum.create(op.get_bind(), checkfirst=True)

    # Alter the gender column, explicitly casting existing values
    op.execute("ALTER TABLE users ALTER COLUMN gender TYPE gender USING gender::gender")

    # Drop the hashed_password column
    op.drop_column('users', 'hashed_password')


def downgrade() -> None:
    """Downgrade schema."""
    # Add the hashed_password column
    op.add_column('users', sa.Column('hashed_password', sa.VARCHAR(), nullable=False))

    # Alter the gender column back to VARCHAR
    op.execute("ALTER TABLE users ALTER COLUMN gender TYPE VARCHAR")

    # Drop the password column
    op.drop_column('users', 'password')

    # Drop the gender enum type
    gender_enum = postgresql.ENUM('Male', 'Female', name='gender')
    gender_enum.drop(op.get_bind(), checkfirst=False)  # Removed checkfirst for explicit dropping
