# coding utf-8

from sqlalchemy import Index

from sqlalchemy.orm import declared_attr

from .table_model import ETableModel


class ELinkModel(ETableModel):
    __abstract__ = True

    @declared_attr
    def __table_args__(cls) -> tuple[Index]:
        return (
            Index(
                f"idx_{cls.__tablename__}_unique",
                *cls.__annotations__.keys(),
                unique=True,
            ),
        )
