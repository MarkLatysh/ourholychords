"""create song table

Revision ID: d527353ce27d
Revises: 49cbbad27704
Create Date: 2025-02-22 22:20:19.754431

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd527353ce27d'
down_revision: Union[str, None] = '49cbbad27704'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'songs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column("text", sa.String(5000), nullable=False),
    )

def downgrade():
    op.drop_table('songs')