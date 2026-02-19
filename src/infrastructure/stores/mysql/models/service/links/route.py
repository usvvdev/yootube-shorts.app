# coding utf-8

from sqlalchemy import (
    Integer,
    ForeignKey,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

# application dependencies

from src.domain.entities import ELinkModel


class ServiceRouteLinks(ELinkModel):
    service_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "services.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    route_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "service_routes.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )
