# coding utf-8

# packages

from sqlalchemy import (
    String,
    Integer,
    ForeignKey,
    CheckConstraint,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from sqlalchemy.dialects.mysql import TINYINT

# application dependencies

from ..common import BaseMixin


class Accounts(BaseMixin):
    username: Mapped[str] = mapped_column(
        String(length=256),
        unique=True,
        nullable=False,
    )

    hashed_password: Mapped[str] = mapped_column(
        String(length=256),
        nullable=False,
    )

    balance: Mapped[int] = mapped_column(
        Integer,
        server_default="0",
        nullable=False,
    )

    is_active: Mapped[int] = mapped_column(
        TINYINT,
        server_default="1",
        nullable=False,
    )

    service_id: Mapped[str] = mapped_column(
        Integer,
        ForeignKey(
            "services.id",
            ondelete="CASCADE",
        ),
        index=True,
        nullable=False,
    )

    user_id: Mapped[str] = mapped_column(
        Integer,
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        index=True,
        nullable=False,
    )

    __table_args__ = (
        CheckConstraint(
            "balance >= 0",
            name="check_accounts_balance_positive",
        ),
    )
