# coding utf-8

# packages

from sqlalchemy import (
    Select,
    select,
)

# application dependencies

from ...models import Accounts

from ...repository import MySQLRepository


class AccountSQLRepository(MySQLRepository[Accounts]):
    _table: type[Accounts] = Accounts

    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(
            table=self._table,
            *args,
            **kwargs,
        )

    def __fetch_query(
        self,
        service_id: int,
        user_id: int,
    ) -> Select[tuple[type[Accounts]]]:
        return (
            select(self._table)
            .where(
                self._table.service_id == service_id,
                self._table.user_id == user_id,
            )
            .order_by(self._table.id)
        )

    async def fetch_all(
        self,
        user_id: int,
        service_id: int,
    ) -> list[type[Accounts]] | None:
        query: Select[tuple[type[Accounts]]] = self.__fetch_query(
            service_id,
            user_id=user_id,
        )
        return await self._fetch(
            query,
            many=True,
        )

    async def fetch(
        self,
        user_id: int,
        service_id: int,
    ) -> type[Accounts] | None:
        query: Select[tuple[type[Accounts]]] = self.__fetch_query(
            service_id,
            user_id=user_id,
        )
        return await self._fetch(
            query,
            many=False,
        )
