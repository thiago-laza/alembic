"""Campo idade na pessoa2

Revision ID: 70be69d705e5
Revises: 4509f3478aee
Create Date: 2024-12-26 10:56:50.237004

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70be69d705e5'
down_revision: Union[str, None] = '4509f3478aee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pessoa2', sa.Column('idade', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pessoa2', 'idade')
    # ### end Alembic commands ###
