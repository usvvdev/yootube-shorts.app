# coding utf-8

# packages

from typing import (
    Any,
    Optional,
)

from pydantic import (
    RootModel,
    ConfigDict,
    SecretStr,
    Field,
    computed_field,
)

from urllib.parse import quote_plus

# application dependencies

from ..common import BaseConfigType

from ...enums.common import EngineType

from src.core.constants import URL_REQUIRED_FIELDS


class DSNOptions(BaseConfigType):
    driver: Optional[str] = Field(
        default=None,
        description="Connection driver (e.g., 'asyncpg' for PostgreSQL)",
    )

    username: Optional[str] = Field(
        default=None,
        description="Connection username",
        exclude=True,
    )

    password: Optional[SecretStr] = Field(
        default=None,
        description="Connection password",
        exclude=True,
    )

    host: Optional[str] = Field(
        default="localhost",
        description="Connection host",
        exclude=True,
    )

    port: Optional[int] = Field(
        default=None,
        description="Connection port",
        exclude=True,
    )

    database: Optional[str] = Field(
        default=None,
        description="Connection database",
        exclude=True,
    )

    @computed_field
    @property
    def url(
        self,
    ) -> str:
        if not all([getattr(self, value) for value in URL_REQUIRED_FIELDS]):
            return ""

        user: str = quote_plus(self.username) if self.username else ""
        pwd: str = quote_plus(self.password.get_secret_value()) if self.password else ""
        credentials: str = f"{user}:{pwd}@" if pwd else f"{user}@" if user else ""

        return f"{self.driver}://{credentials}{self.host}:{self.port}"


class ConnectionOptions(DSNOptions):
    pool_size: Optional[int] = Field(
        default=None,
        description="Base pool size (SQL engines only)",
    )

    max_overflow: Optional[int] = Field(
        default=None,
        description="Overflow pool connections (SQL engines only)",
    )

    echo: Optional[bool] = Field(
        default=None,
        description="Enable SQL debug logging",
    )

    heartbeat: Optional[int] = Field(
        default=None,
        description="Enable heartbeat (RabbitMQ/etc.)",
    )

    @classmethod
    def set_env_options(
        cls,
        engine: EngineType,
        engine_options: dict[str, Any],
    ) -> "ConnectionOptions":
        class Options(cls):
            model_config = ConfigDict(
                env_prefix=f"{engine.upper()}_",
            )

        return Options(**engine_options)


class EngineOptions(RootModel):
    root: dict[EngineType, ConnectionOptions] = Field(
        ...,
        description="Dictionary of connection configurations by engine type",
    )

    def get_options(
        self,
        engine: EngineType,
    ) -> ConnectionOptions:
        engine_options: ConnectionOptions | None = self.root.get(engine)
        if not engine_options:
            raise KeyError(
                f"Engine options for '{engine.value}' not found in configuration",
            )

        return ConnectionOptions.set_env_options(
            engine=engine,
            engine_options=engine_options.model_dump(),
        )

    model_config = ConfigDict(
        use_enum_values=True,
        validate_by_alias=True,
        mode="json",
    )
