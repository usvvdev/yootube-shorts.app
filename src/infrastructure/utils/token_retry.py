# coding utf-8

# packages

from typing import (
    Callable,
    Awaitable,
    TypeVar,
)

# application depencies

from .token_provider import TokenProvider

from src.infrastructure.stores.mysql.models import Accounts


TResult = TypeVar("TResult")


async def with_token_retry(
    func: Callable[[str], Awaitable[TResult]],
    account: type[Accounts],
    provider: TokenProvider,
) -> TResult:
    token = await provider.get_token(account)

    try:
        data = await func(token)

        print("data", data)

        if data.get("ErrCode") != 0:
            await provider.invalidate(account)

            token = await provider.get_token(account)

            return await func(token)

        return data

    except Exception:
        pass
