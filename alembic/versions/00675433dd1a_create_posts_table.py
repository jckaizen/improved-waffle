"""create posts table

Revision ID: 00675433dd1a
Revises: 
Create Date: 2022-08-28 21:57:04.767851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00675433dd1a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
            sa.Column('title', sa.String(), nullable=False))
    

def downgrade() -> None:
    op.drop('posts')
