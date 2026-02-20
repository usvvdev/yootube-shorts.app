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
        alias="email",
    )

    hashed_password: str = Field(
        ...,
        description="",
        alias="password",
    )

    information_sources: str = Field(
        default="https://www.topmediai.com",
        description="",
    )

    source_site: str = Field(
        default="www.topmediai.com",
        description="",
    )

    software_code: int = Field(
        default=0,
        description="",
    )

    @field_validator(
        "hashed_password",
        mode="before",
    )
    @classmethod
    def hash_password(
        cls,
        value: str,
    ) -> str:
        return md5(value.encode()).hexdigest()
