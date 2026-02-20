# coding utf-8

# packages

from uuid import uuid4

from pydantic import Field

# application depencies

from src.domain.types._types.common import BaseModelType


class HeadersDTO(BaseModelType):
    trace_id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="",
        alias="Ai-Trace-Id",
    )

    token: str = Field(
        default=None,
        description="",
        alias="Token",
    )

    accept: str = Field(
        default="application/json, text/plain, */*",
        description="",
    )

    platform: str = Field(
        default="Web",
        description="",
        alias="x-platform",
    )

    content_type: str = Field(
        default="application/json",
        description="",
        alias="content-type",
    )
