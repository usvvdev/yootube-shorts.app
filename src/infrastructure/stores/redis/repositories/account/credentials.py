# coding utf-8

# application dependencies

from ...repository import RedisRepository

from ....mysql.models import Accounts


class AccountCredentialsCacheRepository(RedisRepository[Accounts]):
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
