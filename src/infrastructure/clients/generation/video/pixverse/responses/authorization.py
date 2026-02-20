# coding utf-8

# packages

from pydantic import Field

# application depencies

from src.domain.types._types.common import BaseModelType


class ResultData(BaseModelType):
    token: str = Field(
        ...,
        description="",
        alias="Token",
    )


class AuthorizationData(BaseModelType):
    result: ResultData = Field(
        ...,
        description="",
        alias="Result",
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
