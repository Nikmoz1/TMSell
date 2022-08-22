"""empty message

Revision ID: ff38c7e9ecf3
Revises: 4cb2272f2ab8
Create Date: 2022-08-21 01:01:48.575956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff38c7e9ecf3'
down_revision = '4cb2272f2ab8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bots', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bots', 'is_active')
    # ### end Alembic commands ###
