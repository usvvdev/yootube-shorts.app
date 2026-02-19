# coding utf-8

# packages

from pydantic import Field

# application dependencies

from src.domain.types._types.options import (
    AuthOptions,
    EngineOptions,
    OpenAPIOptions,
    TelegramOptions,
)


class ApplicationOptionsMixin:
    telegram_options: TelegramOptions | None = Field(
        default=None,
        description="Telegram integration options",
    )

    auth_options: AuthOptions | None = Field(
        default=None,
        description="Authentication options",
    )

    engine_options: EngineOptions | None = Field(
        default=None,
        description="Database engine connection options",
    )

    openapi: OpenAPIOptions | None = Field(
        default=None,
        description="Application OpenAPI options",
    )
