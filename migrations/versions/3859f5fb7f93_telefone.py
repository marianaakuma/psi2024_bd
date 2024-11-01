"""telefone

Revision ID: 3859f5fb7f93
Revises: b4fd6106b839
Create Date: 2024-10-29 13:57:31.996838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3859f5fb7f93'
down_revision = 'b4fd6106b839'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('telefone', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_column('telefone')

    # ### end Alembic commands ###
