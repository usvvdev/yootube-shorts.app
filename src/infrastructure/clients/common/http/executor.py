# coding utf-8

# packages

from typing import AsyncGenerator

from contextlib import asynccontextmanager

from httpx import (
    AsyncClient,
    HTTPError,
)

# application dependencies

from src.domain.types._types.options import ServiceOptions


class HTTPExecutor:
    def __init__(
        self,
        *,
        options: ServiceOptions,
    ) -> None:
        self._options = options

    @asynccontextmanager
    async def _open_client(self) -> AsyncGenerator[AsyncClient, None]:
        try:
            async with AsyncClient(
                **self._options.dump,
            ) as client:
                yield client
        except HTTPError as err:
            raise RuntimeError(err)
