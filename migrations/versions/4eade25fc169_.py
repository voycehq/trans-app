"""empty message

Revision ID: 4eade25fc169
Revises: 0353779ec628
Create Date: 2022-03-21 18:12:32.668815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4eade25fc169'
down_revision = '0353779ec628'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'language', ['code'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'language', type_='unique')
    # ### end Alembic commands ###
