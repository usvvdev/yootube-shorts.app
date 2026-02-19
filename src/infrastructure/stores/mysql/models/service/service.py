# coding utf-8

# packages

from sqlalchemy import String

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

# application dependencies

from ..common import BaseMixin

from .mixins import ServiceMixin


class Services(
    BaseMixin,
    ServiceMixin,
):
    title: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        unique=True,
    )

    description: Mapped[str] = mapped_column(
        String(256),
        nullable=False,
    )
