"""Criando compo senha na tabela pessoa

Revision ID: 8a75358ecf69
Revises: 426b167f69fd
Create Date: 2024-12-26 10:10:50.751294

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a75358ecf69'
down_revision: Union[str, None] = '426b167f69fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pessoa', sa.Column('senha', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pessoa', 'senha')
    # ### end Alembic commands ###