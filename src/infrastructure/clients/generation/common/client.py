# coding utf-8

# packages

from typing import (
    Any,
    TypeVar,
)

# application depencies

from ...common.http import BaseHTTPAdapter

from src.domain.types._types.common import BaseModelType

from src.domain.types.enums.common import ServiceEndpoint

from src.infrastructure.stores.mysql.models import Accounts

from src.infrastructure.stores.redis.repositories.account import (
    AccountCredentialsCacheRepository,
)

from src.infrastructure.stores.mysql.repositories.account import (
    AccountSQLRepository,
)

TDto = TypeVar(
    "TDto",
    bound=BaseModelType,
)

TResponse = TypeVar(
    "TResponse",
    bound=BaseModelType,
)


class HTTPClientMixin(BaseHTTPAdapter):
    def __init__(
        self,
        account_reposiotry: AccountSQLRepository,
        account_cache_repository: AccountCredentialsCacheRepository,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)

        self._account_reposiotry = account_reposiotry
        self._account_cache_repository = account_cache_repository

    async def authorization(
        self,
        account: Accounts,
        dto_model: type[TDto],
        response_model: type[TResponse],
        token_extractor: callable,
    ) -> str:
        dto: TDto = dto_model.model_validate(account)

        response: dict[str, Any] = await self.post(
            endpoint=ServiceEndpoint.AUTHORIZATION,
            params=dto.dump,
        )

        parsed: TResponse = response_model(**response)

        token: str = token_extractor(parsed)

        await self._account_cache_repository.set(
            id=account.id,
            value={
                "usage_count": 0,
                "access_token": token,
            },
        )

        return token
