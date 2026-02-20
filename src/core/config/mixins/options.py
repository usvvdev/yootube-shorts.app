# coding utf-8

# packages

from typing import Optional

from pydantic import Field

# application dependencies

from src.domain.types._types.options import (
    AuthOptions,
    EngineOptions,
    OpenAPIOptions,
    TelegramOptions,
    ServiceOptions,
)


class ApplicationOptionsMixin:
    telegram_options: Optional[TelegramOptions] = Field(
        default=None,
        description="Telegram integration options",
    )

    auth_options: Optional[AuthOptions] = Field(
        default=None,
        description="Authentication options",
    )

    engine_options: Optional[EngineOptions] = Field(
        default=None,
        description="Database engine connection options",
    )

    service_options: Optional[ServiceOptions] = Field(
        default=None,
        description="Database engine connection options",
    )

    openapi: Optional[OpenAPIOptions] = Field(
        default=None,
        description="Application OpenAPI options",
    )
