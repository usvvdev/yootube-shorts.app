# coding utf-8

# packages

from typing import Generic

from sqlalchemy import (
    # functions,
    select,
    insert,
    update,
    delete,
    # types,
    Select,
    Insert,
    Update,
    Delete,
)

# application dependencies

from ..base import TTable

from .engine import BaseSQLEngine

from .executor import BaseSQLExecutor

from src.domain.types._types.common import BaseModelType


class BaseSQLRepository(
    BaseSQLExecutor,
    Generic[TTable],
):
    def __init__(
        self,
        *,
        engine: BaseSQLEngine,
        table: type[TTable],
    ) -> None:
        super().__init__(
            engine=engine,
        )
        self._table = table

    async def fetch(
        self,
        query: Select | None = None,
        *,
        many: bool = True,
    ) -> list[TTable] | TTable | None:
        stmt: Select = query if query is not None else select(self._table)
        return await self._fetch(
            stmt,
            many=many,
        )

    async def insert(
        self,
        data: BaseModelType,
    ) -> TTable:
        stmt: Insert = (
            insert(self._table)
            .values(**data.dump)
            .returning(
                self._table,
            )
        )
        return await self._commit(
            stmt,
        )

    async def update(
        self,
        *,
        id: int,
        data: BaseModelType,
    ) -> TTable | None:
        stmt: Update = (
            update(self._table)
            .filter_by(id=id)
            .values(**data.dump)
            .returning(self._table)
        )
        return await self._commit(
            stmt,
        )

    async def delete(
        self,
        *,
        id: int,
    ) -> TTable | None:
        stmt: Delete = (
            delete(self._table)
            .filter_by(id=id)
            .returning(
                self._table,
            )
        )
        return await self._commit(
            stmt,
        )
