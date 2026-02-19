# coding utf-8

# packages

from typing import Any

from httpx import Response

# application dependencies

from .executor import HTTPExecutor

from src.domain.types.enums.common import RequestMethod

from src.domain.types._types.options import ServiceOptions


class BaseHTTPAdapter(HTTPExecutor):
    def __init__(
        self,
        *,
        service: str,
        options: ServiceOptions,
    ) -> None:
        super().__init__(
            options=options,
        )
        self._service = service

    async def __session_request(
        self,
        *,
        method: str,
        url: str,
        **kwargs,
    ) -> Response:
        async with self._open_client() as client:
            return await client.request(
                method=method,
                url=url,
                **kwargs,
            )

    async def __request(
        self,
        *,
        method: str,
        base_url: str,
        endpoint: str,
        **kwargs,
    ) -> Any | None:
        url: str = f"{base_url}{endpoint}"

        response: Response = await self.__session_request(
            method=method,
            url=url,
            **kwargs,
        )
        return response.json() if response.content else None

    async def post(
        self,
        *args,
        **kwargs,
    ) -> Any | None:
        return await self.__request(
            method=RequestMethod.POST,
            *args,
            **kwargs,
        )

    async def get(
        self,
        *args,
        **kwargs,
    ) -> Any | None:
        return await self.__request(
            method=RequestMethod.GET,
            *args,
            **kwargs,
        )
