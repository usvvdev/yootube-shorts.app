# coding utf-8

from re import sub

from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
)

from src.core.constants import (
    SNAKE_CASE_PATTERN,
    SNAKE_CASE_REPLACEMENT,
)


class ETableModel(DeclarativeBase):
    __name__: str

    @declared_attr.directive
    def __tablename__(
        cls,
    ) -> str:
        table_name: str = sub(
            SNAKE_CASE_PATTERN,
            SNAKE_CASE_REPLACEMENT,
            cls.__name__,
        )
        return table_name.lower()
