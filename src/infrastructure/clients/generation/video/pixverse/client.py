# coding utf-8

# packages

from typing import Any

# application depencies

from .dtos import (
    T2VDTO,
    HeadersDTO,
    AuthorizationDTO,
)

from ...common import HTTPClientMixin

from .....utils import with_token_retry

from .adapter import PixverseHTTPAdapter

from .responses import AuthorizationResponse

from src.domain.types.enums.common import ServiceEndpoint

from src.infrastructure.stores.mysql.models.account import Accounts


class PixverseClient(
    PixverseHTTPAdapter,
    HTTPClientMixin,
):
    async def authorization(
        self,
        *args,
        **kwargs,
    ) -> str:
        return await super().authorization(
            dto_model=AuthorizationDTO,
            response_model=AuthorizationResponse,
            token_extractor=lambda r: r.resp.result.token,
            *args,
            **kwargs,
        )

    async def text_to_video(
        self,
        user_id: int,
        prompt: str,
    ):
        account: type[Accounts] | None = await self.fetch_service_account(
            user_id=user_id,
        )

        async def request(
            token: str,
        ) -> dict[str, Any]:
            return await self.post(
                endpoint=ServiceEndpoint.T2V,
                # Request headers
                headers=HeadersDTO(
                    token=token,
                ).dump,
                # Request body
                json=T2VDTO(
                    prompt=prompt,
                ).dump,
            )

        return await with_token_retry(
            request,
            account,
            self._token_provider,
        )
