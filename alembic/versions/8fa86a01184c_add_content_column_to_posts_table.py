"""add content column to posts table

Revision ID: 8fa86a01184c
Revises: 00675433dd1a
Create Date: 2022-08-28 22:03:12.160050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fa86a01184c'
down_revision = '00675433dd1a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts','content')
