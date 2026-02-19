# coding utf-8

# packages

from typing import Generic

# application dependencies

from ..common import (
    TTable,
    BaseCacheRepository,
)

from .engine import RedisEngine

from src.domain.protocols.stores import IRedisProtocol


class RedisRepository(
    BaseCacheRepository,
    IRedisProtocol,
    Generic[TTable],
):
    def __init__(
        self,
        *,
        engine: RedisEngine,
        table: type[TTable],
    ) -> None:
        super().__init__(
            engine=engine,
            table=table,
        )
