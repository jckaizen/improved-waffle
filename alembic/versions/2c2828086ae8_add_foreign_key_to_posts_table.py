"""add foreign-key to posts table

Revision ID: 2c2828086ae8
Revises: bdb962a64da9
Create Date: 2022-08-28 22:14:02.410973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c2828086ae8'
down_revision = 'bdb962a64da9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk',source_table="posts",referent_table="users",
            local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
    pass
