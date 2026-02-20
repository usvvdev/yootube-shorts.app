# coding utf-8

# packages

from sqlalchemy import (
    Select,
    select,
)

from sqlalchemy.orm import selectinload

# application dependencies

from ...models import Services

from ...repository import MySQLRepository


class ServiceSQLRepository(MySQLRepository[Services]):
    _table: type[Services] = Services

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

    async def fetch_routes(
        self,
        service_id: int,
    ) -> list[type[Services]] | None:
        query: Select[tuple[type[Services]]] = (
            select(self._table)
            .options(selectinload(self._table.routes))
            .where(
                self._table.id == service_id,
            )
        )
        service: type[Services] | None = await self.fetch(
            query,
            many=False,
        )
        return service.routes if service else None

    async def fetch_id(
        self,
        service_title: str,
    ) -> int | None:
        query: Select[tuple[type[Services]]] = select(self._table).where(
            self._table.title == service_title,
        )
        service: type[Services] | None = await self.fetch(
            query,
            many=False,
        )
        return service.id if service else None
