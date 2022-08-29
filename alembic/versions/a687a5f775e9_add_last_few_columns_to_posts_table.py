"""add last few columns to posts table

Revision ID: a687a5f775e9
Revises: 2c2828086ae8
Create Date: 2022-08-28 22:19:33.339249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a687a5f775e9'
down_revision = '2c2828086ae8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'))
    op.add_column('posts',sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,
        server_default=sa.text('NOW()')))


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
