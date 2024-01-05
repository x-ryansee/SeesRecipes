"""Add fields for mealTypes, diets, and cuisine

Revision ID: d91d00ce5ba9
Revises: 71963b9e65ca
Create Date: 2024-01-05 11:42:31.173947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd91d00ce5ba9'
down_revision = '71963b9e65ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mealTypes', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('diets', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('cuisine', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.drop_column('cuisine')
        batch_op.drop_column('diets')
        batch_op.drop_column('mealTypes')

    # ### end Alembic commands ###
