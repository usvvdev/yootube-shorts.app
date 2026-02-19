# coding utf-8

# packages

from sqlalchemy import (
    Select,
    select,
)

# application dependencies

from ...models import AccountCredentials

from ...repository import MySQLRepository


class AccountCredentialsSQLRepository(MySQLRepository[AccountCredentials]):
    _table: type[AccountCredentials] = AccountCredentials

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

    async def fetch_by_account_id(
        self,
        account_id: int,
    ) -> list[type[AccountCredentials]] | None:
        query: Select[tuple[type[AccountCredentials]]] = (
            select(self._table)
            .where(
                self._table.account_id == account_id,
            )
            .order_by(self._table.id)
        )
        return await self._fetch(
            query,
            many=True,
        )
