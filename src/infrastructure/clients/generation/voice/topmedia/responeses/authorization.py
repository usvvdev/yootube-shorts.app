# coding utf-8

# packages

from pydantic import Field

# application depencies

from src.domain.types._types.common import BaseModelType


class AuthorizationData(BaseModelType):
    token: str = Field(
        ...,
        description="",
    )


class AuthorizationResponse(BaseModelType):
    data: AuthorizationData = Field(
        ...,
        description="",
    )
