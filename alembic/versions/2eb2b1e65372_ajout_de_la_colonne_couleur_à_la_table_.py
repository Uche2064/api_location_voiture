"""ajout de la colonne couleur à la table car

Revision ID: 2eb2b1e65372
Revises: b51b1ddf9558
Create Date: 2024-04-10 12:22:14.204872

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2eb2b1e65372'
down_revision: Union[str, None] = 'b51b1ddf9558'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cars', sa.Column('couleur', sa.String(length=150), nullable=False))
    op.create_index(op.f('ix_cars_couleur'), 'cars', ['couleur'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cars_couleur'), table_name='cars')
    op.drop_column('cars', 'couleur')
    # ### end Alembic commands ###
