# coding utf-8

# application dependencies

from ..common import BaseCacheEngine

from src.core.config import ApplicationBaseConfig

from src.domain.types.enums.common import EngineType


class RedisEngine(BaseCacheEngine):
    _name: str = EngineType.REDIS

    def __init__(
        self,
        *,
        config: ApplicationBaseConfig,
    ) -> None:
        super().__init__(
            name=self._name,
            config=config,
        )
