"""project setup

Revision ID: e93a787ad4ca
Revises: 
Create Date: 2022-03-19 08:31:46.607629

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e93a787ad4ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('date',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_date', sa.DateTime(), nullable=False),
    sa.Column('date_full_name', sa.String(length=100), nullable=False),
    sa.Column('date_key', sa.String(length=100), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('is_leap_year', sa.Boolean(), nullable=True),
    sa.Column('month_number', sa.Integer(), nullable=False),
    sa.Column('month_name', sa.String(length=100), nullable=False),
    sa.Column('year_week', sa.Integer(), nullable=False),
    sa.Column('day_of_week', sa.Integer(), nullable=False),
    sa.Column('day_of_month', sa.Integer(), nullable=False),
    sa.Column('day_of_year', sa.Integer(), nullable=False),
    sa.Column('day_name', sa.String(length=100), nullable=False),
    sa.Column('is_working_day', sa.Boolean(), nullable=False),
    sa.Column('quarter', sa.Integer(), nullable=False),
    sa.Column('Year_half', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('deleted_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workspace_role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('deleted_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('language',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('deleted_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['date_id'], ['date.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('language_setting',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_id', sa.Integer(), nullable=False),
    sa.Column('language_id', sa.Integer(), nullable=False),
    sa.Column('details', mysql.JSON(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('deleted_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['date_id'], ['date.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('default_language', sa.Integer(), nullable=True),
    sa.Column('date_id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('deleted_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['date_id'], ['date.id'], ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['default_language'], ['language.id'], ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workspace',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('customer_count', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('deleted_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('text',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('language_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('reviewed_by', sa.Integer(), nullable=True),
    sa.Column('workspace', sa.Integer(), nullable=True),
    sa.Column('date_id', sa.Integer(), nullable=False),
    sa.Column('reviewed_date', sa.DateTime(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('deleted_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ondelete='NO ACTION'),
    sa.ForeignKeyConstraint(['date_id'], ['date.id'], ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['language_id'], ['language.id'], ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['reviewed_by'], ['customer.id'], ondelete='NO ACTION'),
    sa.ForeignKeyConstraint(['workspace'], ['workspace.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workspace_detail',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('workspace_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('workspace_role_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('deleted_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['workspace_id'], ['workspace.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['workspace_role_id'], ['workspace_role.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('translated_text',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text_id', sa.Integer(), nullable=False),
    sa.Column('language_id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('reviewed_by', sa.Integer(), nullable=True),
    sa.Column('reviewed_date', sa.DateTime(), nullable=True),
    sa.Column('translated_date', sa.DateTime(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('deleted_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['language_id'], ['language.id'], ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['reviewed_by'], ['customer.id'], ondelete='NO ACTION'),
    sa.ForeignKeyConstraint(['text_id'], ['text.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('translated_text')
    op.drop_table('workspace_detail')
    op.drop_table('text')
    op.drop_table('workspace')
    op.drop_table('customer')
    op.drop_table('language_setting')
    op.drop_table('language')
    op.drop_table('workspace_role')
    op.drop_table('date')
    # ### end Alembic commands ###
