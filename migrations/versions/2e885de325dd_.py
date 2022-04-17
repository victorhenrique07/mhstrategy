"""empty message

Revision ID: 2e885de325dd
Revises: d74de3459d6c
Create Date: 2022-04-17 13:13:57.736798

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2e885de325dd'
down_revision = 'd74de3459d6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('usernametwo', table_name='users')
    op.drop_column('users', 'usernametwo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('usernametwo', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=45), nullable=False))
    op.create_index('usernametwo', 'users', ['usernametwo'], unique=False)
    # ### end Alembic commands ###