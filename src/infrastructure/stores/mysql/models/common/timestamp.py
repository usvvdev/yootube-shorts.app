# coding utf-8

# packages

from typing import ClassVar

from sqlalchemy import (
    DateTime,
    func,
)

from sqlalchemy.orm import (
    Mapped,
    declared_attr,
    mapped_column,
)

from datetime import datetime


class TimestampMixin:
    # default values for mixin flags
    __created_at__: ClassVar[bool] = True
    __updated_at__: ClassVar[bool] = False
    __last_used_at__: ClassVar[bool] = False

    @declared_attr
    def created_at(cls) -> Mapped[datetime]:
        if not cls.__created_at__:
            return None
        return mapped_column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=False,
        )

    @declared_attr
    def updated_at(cls) -> Mapped[datetime]:
        if not cls.__updated_at__:
            return None
        return mapped_column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )

    @declared_attr
    def last_used_at(cls) -> Mapped[datetime]:
        if not cls.__last_used_at__:
            return None
        return mapped_column(
            DateTime(timezone=True),
            nullable=True,
        )
