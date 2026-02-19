# coding utf-8

# packages

from sqlalchemy import (
    Select,
    select,
)

from sqlalchemy.orm import selectinload

# application dependencies

from ...models import (
    Users,
    Services,
)

from ...repository import MySQLRepository


class UserRepository(MySQLRepository[Users]):
    _table: type[Users] = Users

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

    async def fetch_by_username(
        self,
        username: str,
    ) -> Users | None:
        query: Select[tuple[type[Users]]] = select(self._table).where(
            self._table.username == username,
        )
        return await self.fetch(
            query,
            many=False,
        )

    async def fetch_services(
        self,
        auth_user_id: int,
    ) -> list[type[Services]] | None:
        query: Select[tuple[type[Users]]] = (
            select(self._table)
            .options(selectinload(self._table.services))
            .where(
                self._table.id == auth_user_id,
            )
        )
        user: type[Users] | None = await self.fetch(
            query,
            many=False,
        )
        return user.services if user else None
