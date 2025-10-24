"""alter users table

Revision ID: c831d02156c1
Revises: 
Create Date: 2025-10-23 11:22:24.848438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c831d02156c1'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute('''
               ALTER TABLE users
                   ADD COLUMN userType
                   ENUM ('student', 'teacher', 'admin')
                   NOT NULL DEFAULT 'student'
               ''')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute('''ALTER TABLE users DROP COLUMN userType''')
    pass
