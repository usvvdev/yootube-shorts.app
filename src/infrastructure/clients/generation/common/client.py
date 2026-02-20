# coding utf-8

# packages

from typing import (
    Any,
    TypeVar,
)

# application depencies

from ....utils import TokenProvider

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

from src.infrastructure.stores.mysql.repositories.service import (
    ServiceSQLRepository,
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
        account_repository: AccountSQLRepository,
        account_cache_repository: AccountCredentialsCacheRepository,
        service_repository: ServiceSQLRepository,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)

        self._account_repository = account_repository
        self._account_cache_repository = account_cache_repository
        self._service_repository = service_repository

        self._token_provider = TokenProvider(
            cache_repo=self._account_cache_repository,
            auth_strategy=self.authorization,
        )

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

        print(parsed)

        token: str = token_extractor(parsed)

        await self._account_cache_repository.set(
            id=account.id,
            value={
                "usage_count": 0,
                "access_token": token,
            },
        )

        return token

    async def fetch_service_id(
        self,
        service_title: str,
    ) -> int | None:
        return await self._service_repository.fetch_id(service_title=service_title)

    async def fetch_service_account(
        self,
        user_id: int,
    ) -> type[Accounts] | None:
        service_id = await self.fetch_service_id(
            service_title=self._service,
        )

        return await self._account_repository.fetch(
            user_id,
            service_id=service_id,
        )
