# coding utf-8

# packages

from typing import ClassVar

from sqlalchemy import (
    Integer,
    String,
    Enum,
    ForeignKey,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

# application dependencies

from ..common import (
    BaseMixin,
    TimestampMixin,
)

from src.domain.types.enums.user import UserGenerationStatus


class UserGenerations(
    BaseMixin,
    TimestampMixin,
):
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        index=True,
        nullable=False,
    )

    service_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "services.id",
            ondelete="CASCADE",
        ),
        index=True,
        nullable=False,
    )

    account_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "accounts.id",
            ondelete="CASCADE",
        ),
        index=True,
        nullable=False,
    )

    result: Mapped[str] = mapped_column(
        String(512),
        nullable=True,
    )

    status: Mapped[UserGenerationStatus] = mapped_column(
        Enum(
            UserGenerationStatus,
            native_enum=False,
        ),
        nullable=False,
        default=UserGenerationStatus.PENDING,
    )

    __updated_at__: ClassVar[bool] = True
