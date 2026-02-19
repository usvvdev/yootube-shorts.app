# coding utf-8

# application dependencies

from ..common import BaseSQLEngine

from src.core.config import ApplicationBaseConfig

from src.domain.types.enums.common import EngineType


class MySQLEngine(BaseSQLEngine):
    _name: str = EngineType.MYSQL

    def __init__(
        self,
        *,
        config: ApplicationBaseConfig,
    ) -> None:
        super().__init__(
            name=self._name,
            config=config,
        )
