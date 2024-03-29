"""empty message

Revision ID: 23473ee052ed
Revises: 
Create Date: 2019-08-04 11:34:31.525759

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '23473ee052ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('name', mysql.CHAR(charset='gbk', collation='gbk_chinese_ci', length=20), nullable=True),
    sa.Column('sec', mysql.CHAR(charset='gbk', collation='gbk_chinese_ci', length=20), nullable=True),
    sa.Column('age', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
