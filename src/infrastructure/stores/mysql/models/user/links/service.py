# coding utf-8

# packages

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


class UserServiceLinks(ELinkModel):
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    service_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "services.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )
