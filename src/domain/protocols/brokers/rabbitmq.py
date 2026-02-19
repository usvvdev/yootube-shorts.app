# coding utf-8

from typing import Protocol

from faststream.rabbit import RabbitBroker

from aio_pika import RobustConnection


class IRabbitMQProtocol(Protocol):
    async def broker(
        self,
    ) -> RabbitBroker: ...

    async def connect(
        self,
    ) -> RobustConnection: ...
