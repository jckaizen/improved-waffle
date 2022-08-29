"""add user table

Revision ID: bdb962a64da9
Revises: 8fa86a01184c
Create Date: 2022-08-28 22:07:14.299312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdb962a64da9'
down_revision = '8fa86a01184c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
            sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
            sa.Column('email',sa.String(),nullable=False),
            sa.Column('password',sa.String(),nullable=False),
            sa.Column('created_at',sa.TIMESTAMP(timezone=True),
                server_default=sa.text('now()'),nullable=False),
            sa.UniqueConstraint('email')
            ) 


def downgrade() -> None:
    op.drop_table('users')
