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

    async def fetch_all(
        self,
        service_id: int,
        auth_user_id: int,
    ) -> list[type[Accounts]] | None:
        query: Select[tuple[type[Accounts]]] = (
            select(self._table)
            .where(
                self._table.service_id == service_id,
                self._table.auth_user_id == auth_user_id,
            )
            .order_by(self._table.id)
        )
        return await self._fetch(
            query,
            many=True,
        )
