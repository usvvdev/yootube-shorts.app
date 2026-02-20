# coding utf-8

# packages

from hashlib import md5

from pydantic import (
    Field,
    field_validator,
)

# application depencies

from src.domain.types._types.common import BaseModelType


class AuthorizationDTO(BaseModelType):
    username: str = Field(
        ...,
        description="",
        alias="Username",
    )

    hashed_password: str = Field(
        ...,
        description="",
        alias="Password",
    )
