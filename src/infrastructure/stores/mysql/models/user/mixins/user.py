# coding utf-8

from sqlalchemy.orm import (
    declared_attr,
    relationship,
)


class UserMixin:
    @declared_attr
    def services(cls):
        return relationship(
            "Services",
            secondary="user_service_links",
            back_populates="users",
        )
