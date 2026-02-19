# coding utf-8

# application dependencies

from ...models import UserGenerations

from ...repository import MySQLRepository


class UserGenerationSQLRepository(MySQLRepository[UserGenerations]):
    _table: type[UserGenerations] = UserGenerations

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
