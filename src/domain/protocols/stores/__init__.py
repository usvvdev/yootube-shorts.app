# coding utf-8

from .mysql import IMySQLProtocol

from .redis import IRedisProtocol

__all__: list[str] = [
    "IRedisProtocol",
    "IMySQLProtocol",
]
