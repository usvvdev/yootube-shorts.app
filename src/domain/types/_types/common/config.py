# coding utf-8

# packages

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

# application dependencies

from src.core.constants import (
    ENV_FILE,
    ENV_PREFIX,
)


class BaseConfigType(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix=ENV_PREFIX,
        env_file=ENV_FILE,
        validate_assignment=True,
        use_enum_values=True,
        extra="ignore",
    )
