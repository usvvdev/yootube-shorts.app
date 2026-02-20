# coding utf-8

# packages

# application depencies

from .dtos import AuthorizationDTO

from ...common import HTTPClientMixin

from .adapter import TopMediaHTTPAdapter

from .responeses import AuthorizationResponse


class TopMediaClient(
    HTTPClientMixin,
    TopMediaHTTPAdapter,
):
    async def account_authorization(
        self,
        *args,
        **kwargs,
    ) -> str:
        return await self.authorization(
            dto_model=AuthorizationDTO,
            response_model=AuthorizationResponse,
            token_extractor=lambda r: r.data.token,
            *args,
            **kwargs,
        )
