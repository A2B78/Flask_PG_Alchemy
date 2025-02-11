"""empty message

Revision ID: 17b375591424
Revises: 48471f866060
Create Date: 2025-02-11 16:39:38.383902

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy.dialects import postgresql

# Révision identifiant et suivants
revision = '17b375591424'
down_revision = '48471f866060'
branch_labels = None
depends_on = None

def upgrade():
    # Ajoutez des colonnes avec des valeurs par défaut
    with op.batch_alter_table('user') as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=False, server_default='default@example.com'))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    with op.batch_alter_table('user_session') as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # Mettre à jour les colonnes après l'ajout
    op.execute(
        sa.table('user',
            sa.column('email', sa.String(length=120))
        ).update().values({'email': 'default@example.com'})
    )

def downgrade():
    with op.batch_alter_table('user') as batch_op:
        batch_op.drop_column('email')
        batch_op.drop_column('created_at')
        batch_op.drop_column('updated_at')

    with op.batch_alter_table('user_session') as batch_op:
        batch_op.drop_column('updated_at')