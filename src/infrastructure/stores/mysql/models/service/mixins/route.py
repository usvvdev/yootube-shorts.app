# coding utf-8

from sqlalchemy.orm import (
    declared_attr,
    relationship,
)


class ServiceRouteMixin:
    @declared_attr
    def services(cls):
        return relationship(
            "Services",
            secondary="service_route_links",
            back_populates="routes",
        )
