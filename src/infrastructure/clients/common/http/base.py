# coding utf-8

# packages

from typing import (
    Any,
    Optional,
)

from httpx import Response

from functools import lru_cache

# application dependencies

from .executor import HTTPExecutor

from src.domain.types.enums.common import ServiceType

from src.domain.types.enums.common import RequestMethod

from src.core.config.base import ApplicationBaseConfig

from src.domain.types._types.options import ServiceURLOptions


class BaseHTTPAdapter(HTTPExecutor):
    def __init__(
        self,
        *,
        service: ServiceType,
        config: ApplicationBaseConfig,
    ) -> None:
        self._config = config
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

    @property
    @lru_cache
    def service_options(
        self,
    ) -> ServiceURLOptions:
        return self._config.service_options.get_options(
            self._service,
        )

    async def __request(
        self,
        *,
        method: str,
        endpoint: str,
        **kwargs,
    ) -> Optional[Any]:
        url: str = self.service_options.build_url(
            endpoint=endpoint,
        )
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
    ) -> Optional[Any]:
        return await self.__request(
            method=RequestMethod.POST,
            *args,
            **kwargs,
        )

    async def get(
        self,
        *args,
        **kwargs,
    ) -> Optional[Any]:
        return await self.__request(
            method=RequestMethod.GET,
            *args,
            **kwargs,
        )
