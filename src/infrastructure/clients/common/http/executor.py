# coding utf-8

# packages

from typing import AsyncGenerator

from contextlib import asynccontextmanager

from httpx import (
    AsyncClient,
    HTTPError,
)

# application dependencies


class HTTPExecutor:
    # def __init__(
    #     self,
    #     *,
    #     timeout: int = 60,
    # ) -> None:
    #     self._timeout = timeout

    @asynccontextmanager
    async def _open_client(self) -> AsyncGenerator[AsyncClient, None]:
        try:
            async with AsyncClient(
                timeout=60,
            ) as client:
                yield client
        except HTTPError as err:
            raise RuntimeError(err)
