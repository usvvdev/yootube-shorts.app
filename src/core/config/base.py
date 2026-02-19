# coding utf-8

# packages

from pydantic import (
    Field,
    computed_field,
)

from os import getenv

from logging import INFO

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
)

# application dependencies

from ..constants import (
    JSON_FILE,
    ENV_PREFIX,
)

from .mixins import ApplicationOptionsMixin

from src.domain.types.enums.common import AppMode

from src.domain.types._types.common import BaseConfigType

from src.domain.types._types.source import (
    EnvironmentJsonConfigSettingsSource,
)


class ApplicationBaseConfig(
    BaseConfigType,
    ApplicationOptionsMixin,
):
    mode: AppMode = Field(
        ...,
        description="Application running mode.",
        exclude=True,
    )

    # Logging level/loggers settings
    logging_level: int = Field(
        default=INFO,
        description="Default logging level",
    )

    loggers: tuple[str, ...] = Field(
        default=("uvicorn.asgi", "uvicorn.access"),
        description="Tuple of logger names to configure",
    )

    # API settings
    api_prefix: str = Field(
        default="/api",
        exclude=True,
        description="The prefix for all API routes.",
    )

    api_version: str = Field(
        ...,
        exclude=True,
        description="The version of the API used in route paths.",
    )

    @computed_field
    @property
    def api_path(
        self,
    ) -> str:
        if self.api_version:
            return f"{self.api_prefix}/v{self.api_version}"
        return self.api_prefix

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        mode: str = getenv(
            f"{ENV_PREFIX}MODE",
            AppMode.DEVELOPMENT,
        )

        sources: tuple[PydanticBaseSettingsSource, ...] = (
            init_settings,
            env_settings,
            dotenv_settings,
            EnvironmentJsonConfigSettingsSource(
                settings_cls,
                JSON_FILE,
                mode,
            )
            if mode
            else None,
            file_secret_settings,
        )

        return tuple(
            filter(
                None,
                map(lambda x: x, sources),
            )
        )
