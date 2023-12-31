"""create tables

Revision ID: adc29bb302ac
Revises: a9fa9cfcbef4
Create Date: 2023-11-13 03:03:23.998069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adc29bb302ac'
down_revision = 'a9fa9cfcbef4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant_pizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pizza_id', sa.Integer(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['pizza_id'], ['pizzas.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('restaurantPizza')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurantPizza',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('price', sa.INTEGER(), nullable=False),
    sa.Column('pizza_id', sa.INTEGER(), nullable=True),
    sa.Column('restaurant_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['pizza_id'], ['pizzas.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('restaurant_pizzas')
    # ### end Alembic commands ###
