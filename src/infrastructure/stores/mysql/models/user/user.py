# coding utf-8

# packages

from sqlalchemy import (
    String,
    Enum,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from sqlalchemy.dialects.mysql import TINYINT

# application dependencies

from ..common import (
    BaseMixin,
    TimestampMixin,
)

from .mixins import UserMixin

from src.domain.types.enums.user import UserRole


class Users(
    BaseMixin,
    TimestampMixin,
    UserMixin,
):
    username: Mapped[str] = mapped_column(
        String(length=32),
        nullable=False,
        unique=True,
    )

    role: Mapped[UserRole] = mapped_column(
        Enum(
            UserRole,
            native_enum=False,
        ),
        default=UserRole.USER,
        nullable=False,
    )

    hashed_password: Mapped[str] = mapped_column(
        String(length=256),
        nullable=False,
    )

    is_active: Mapped[int] = mapped_column(
        TINYINT,
        server_default="1",
        nullable=False,
    )
