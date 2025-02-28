"""empty message

Revision ID: ff49386697dd
Revises: fd9422508d1e
Create Date: 2025-02-14 22:25:01.386667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff49386697dd'
down_revision = 'fd9422508d1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cursos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('lugar', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('habilidades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('nivel', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('habilidades')
    op.drop_table('cursos')
    # ### end Alembic commands ###
