"""add_user_and_profile_relation

Revision ID: 3f54d71fe1ba
Revises: e18f52210bf5
Create Date: 2026-06-18 16:48:42.477656
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '3f54d71fe1ba'
down_revision: Union[str, Sequence[str], None] = 'e18f52210bf5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('profile') as batch_op:
        batch_op.alter_column('first_name', existing_type=sa.VARCHAR(), nullable=True)
        batch_op.alter_column('last_name', existing_type=sa.VARCHAR(), nullable=True)
        batch_op.alter_column('gender', existing_type=sa.VARCHAR(), nullable=True)
        batch_op.alter_column('avatar_url', existing_type=sa.VARCHAR(), nullable=True)
        batch_op.alter_column('bio', existing_type=sa.VARCHAR(), nullable=True)
        batch_op.alter_column('dob', existing_type=sa.DATE(), nullable=True)
        batch_op.alter_column('height', existing_type=sa.INTEGER(), nullable=True)
        batch_op.alter_column('weight', existing_type=sa.INTEGER(), nullable=True)
        batch_op.create_unique_constraint('uq_profile_user_id', ['user_id'])
        batch_op.create_foreign_key('fk_profile_user_id', 'user', ['user_id'], ['id'])

    with op.batch_alter_table('user') as batch_op:
        batch_op.alter_column('fingerprint', existing_type=sa.VARCHAR(), type_=sa.Uuid(), existing_nullable=False)


def downgrade() -> None:
    with op.batch_alter_table('user') as batch_op:
        batch_op.alter_column('fingerprint', existing_type=sa.Uuid(), type_=sa.VARCHAR(), existing_nullable=False)

    with op.batch_alter_table('profile') as batch_op:
        batch_op.drop_constraint('fk_profile_user_id', type_='foreignkey')
        batch_op.drop_constraint('uq_profile_user_id', type_='unique')
        batch_op.alter_column('weight', existing_type=sa.INTEGER(), nullable=False)
        batch_op.alter_column('height', existing_type=sa.INTEGER(), nullable=False)
        batch_op.alter_column('dob', existing_type=sa.DATE(), nullable=False)
        batch_op.alter_column('bio', existing_type=sa.VARCHAR(), nullable=False)
        batch_op.alter_column('avatar_url', existing_type=sa.VARCHAR(), nullable=False)
        batch_op.alter_column('gender', existing_type=sa.VARCHAR(), nullable=False)
        batch_op.alter_column('last_name', existing_type=sa.VARCHAR(), nullable=False)
        batch_op.alter_column('first_name', existing_type=sa.VARCHAR(), nullable=False)