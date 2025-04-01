"""add hashed_password

Revision ID: 089d22fbc9b0
Revises: d527353ce27d
Create Date: 2025-03-31 19:51:53.211415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '089d22fbc9b0'
down_revision: Union[str, None] = 'd527353ce27d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("hashed_password", sa.String(100), nullable=False))


def downgrade() -> None:
    op.drop_column("users", "hashed_password")
