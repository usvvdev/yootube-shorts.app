# coding utf-8

# packages

from typing import TypeVar

# application dependencies

from src.domain.entities import ETableModel

from src.core.config import ApplicationBaseConfig

from src.domain.types._types.options import ConnectionOptions


TTable = TypeVar("TTable", bound=ETableModel)


class BaseEngine:
    def __init__(
        self,
        *,
        name: str,
        config: ApplicationBaseConfig,
    ) -> None:
        self._name = name
        self._config = config

    @property
    def options(self) -> ConnectionOptions:
        return self._config.engine_options.get_options(
            self._name,
        )
