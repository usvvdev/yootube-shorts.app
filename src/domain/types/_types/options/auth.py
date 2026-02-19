# coding utf-8

# packages

from pydantic import Field

# application dependencies

from ..common import BaseModelType


class AuthOptions(BaseModelType):
    algorithm: str | None = Field(
        default=None,
        description="Algorithm for both encoding and decoding JWT token.",
    )

    secret_key: str | None = Field(
        default=None,
        description="Secret key used for signing JWT tokens.",
    )
