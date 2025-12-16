"""Initial migration

Revision ID: 3a71a719b74b
Revises: 491bcd6e40d0
Create Date: 2025-12-16 12:47:28.740077

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3a71a719b74b"
down_revision: Union[str, Sequence[str], None] = "491bcd6e40d0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
