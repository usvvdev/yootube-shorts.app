# coding utf-8

# packages

# application depencies

from .dtos import AuthorizationDTO

from ...common import HTTPClientMixin

from .adapter import TopMediaHTTPAdapter

from .responses import AuthorizationResponse

from src.domain.types.enums.common import ServiceEndpoint

from src.infrastructure.stores.mysql.models.account import Accounts


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

    async def text_to_voice(
        self,
        user_id: int,
    ):
        account: type[Accounts] | None = await self.fetch_service_account(
            user_id=user_id,
        )

        if account is None:
            pass
