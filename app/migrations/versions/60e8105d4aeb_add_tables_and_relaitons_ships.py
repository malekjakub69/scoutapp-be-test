"""Add tables and relaitons ships

Revision ID: 60e8105d4aeb
Revises: 83af0e5c2b50
Create Date: 2023-10-28 16:23:33.796306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60e8105d4aeb'
down_revision = '83af0e5c2b50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('troop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('code', sa.Integer(), nullable=False),
    sa.Column('troop_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['troop_id'], ['troop.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('code', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('troop_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['troop_id'], ['troop.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('current_troop_id', sa.Integer(), nullable=True))
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.create_unique_constraint(None, ['login'])
        batch_op.create_foreign_key(None, 'troop', ['current_troop_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.drop_column('current_troop_id')

    op.drop_table('role')
    op.drop_table('troop')
    # ### end Alembic commands ###