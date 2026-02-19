# coding utf-8

# packages

from sqlalchemy import String

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

# application dependencies

from ..common import BaseMixin

from .mixins import ServiceRouteMixin


class ServiceRoutes(
    BaseMixin,
    ServiceRouteMixin,
):
    path: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )
