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
    err_code: int = Field(
        ...,
        description="",
        alias="ErrCode",
    )

    err_msg: str | None = Field(
        default=None,
        description="",
        alias="ErrMsg",
    )

    resp: AuthorizationData = Field(
        default=None,
        description="",
        alias="Resp",
    )
