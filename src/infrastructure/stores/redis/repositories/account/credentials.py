# coding utf-8

# application dependencies

from ...repository import RedisRepository

from ....mysql.models import AccountCredentials


class AccountCredentialsCacheRepository(RedisRepository[AccountCredentials]):
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
