# coding utf-8

from sqlalchemy.orm import (
    declared_attr,
    relationship,
)


class ServiceMixin:
    @declared_attr
    def users(cls):
        return relationship(
            "Users",
            secondary="user_service_links",
            back_populates="services",
        )

    @declared_attr
    def routes(cls):
        return relationship(
            "ServiceRoutes",
            secondary="service_route_links",
            back_populates="services",
        )
