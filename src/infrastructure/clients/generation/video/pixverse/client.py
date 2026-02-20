# coding utf-8

# packages

# application depencies

from .dtos import AuthorizationDTO

from .adapter import PixverseHTTPAdapter

from .responeses import AuthorizationResponse

from ...common import HTTPClientMixin


class PixverseClient(
    PixverseHTTPAdapter,
    HTTPClientMixin,
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
