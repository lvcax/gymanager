"""empty message

Revision ID: cd82f41ab451
Revises: a874dd16351a
Create Date: 2023-04-18 15:14:18.223235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd82f41ab451'
down_revision = 'a874dd16351a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('registration', sa.String(length=6), nullable=False),
    sa.Column('name', sa.String(length=130), nullable=False),
    sa.Column('birth_date', sa.DateTime(), nullable=False),
    sa.Column('address', sa.String(length=150), nullable=False),
    sa.Column('cpf', sa.String(length=15), nullable=False),
    sa.Column('phone_number', sa.String(length=11), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    with op.batch_alter_table('customers', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_customers_registration'), ['registration'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customers', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_customers_registration'))

    op.drop_table('customers')
    # ### end Alembic commands ###
