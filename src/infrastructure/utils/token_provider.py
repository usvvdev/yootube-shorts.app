# coding utf-8

# packages

from typing import (
    Callable,
    Awaitable,
)

# application depencies

from ..stores.mysql.models import Accounts

from ..stores.redis.repositories.account import AccountCredentialsCacheRepository


class TokenProvider:
    def __init__(
        self,
        cache_repo: AccountCredentialsCacheRepository,
        auth_strategy: Callable[[Accounts], Awaitable[str]],
    ):
        self.cache = cache_repo
        self.auth_strategy = auth_strategy

    async def get_token(self, account: Accounts) -> str:
        cached = await self.cache.get(account.id)

        if cached:
            return cached["access_token"]

        return await self.refresh(account)

    async def refresh(
        self,
        account: Accounts,
    ) -> str:
        token = await self.auth_strategy(account)

        await self.cache.set(
            id=account.id,
            value={"access_token": token},
        )

        return token

    async def invalidate(
        self,
        account: Accounts,
    ) -> None:
        await self.cache.delete(
            account.id,
        )
