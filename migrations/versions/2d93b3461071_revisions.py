"""revisions

Revision ID: 2d93b3461071
Revises: cc6c6499cec2
Create Date: 2023-11-14 19:31:21.935507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d93b3461071'
down_revision: Union[str, None] = 'cc6c6499cec2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_accounts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('firstName', sa.String(), nullable=True),
    sa.Column('lastName', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('users')
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.create_foreign_key(None, 'orders', 'user_accounts', ['customer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.create_foreign_key(None, 'orders', 'users', ['customer_id'], ['customer_id'])
    op.create_table('users',
    sa.Column('customer_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('username', sa.VARCHAR(), nullable=True),
    sa.Column('password', sa.VARCHAR(), nullable=True),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('phone_number', sa.VARCHAR(), nullable=True),
    sa.Column('address', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('customer_id'),
    sa.UniqueConstraint('username', 'password', 'email', 'phone_number')
    )
    op.drop_table('user_accounts')
    # ### end Alembic commands ###
