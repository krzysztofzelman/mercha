"""Add payment fields to orders table.

Revision ID: 002
Revises: 001
Create Date: 2026-05-23
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "002"
down_revision: Union[str, None] = "001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TYPE payment_status AS ENUM ('unpaid', 'pending', 'paid', 'failed', 'refunded')")
    op.add_column("orders", sa.Column("payment_status", sa.Enum("unpaid", "pending", "paid", "failed", "refunded", name="payment_status"), server_default="unpaid", nullable=False))
    op.add_column("orders", sa.Column("payment_method", sa.String(50), server_default="", nullable=False))
    op.add_column("orders", sa.Column("payment_id", sa.String(255), server_default="", nullable=False))


def downgrade() -> None:
    op.drop_column("orders", "payment_id")
    op.drop_column("orders", "payment_method")
    op.drop_column("orders", "payment_status")
    op.execute("DROP TYPE IF EXISTS payment_status")
