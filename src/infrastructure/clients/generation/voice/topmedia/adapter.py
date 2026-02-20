# coding utf-8

# application depencies

from ....common.http import BaseHTTPAdapter

from src.domain.types.enums.common import ServiceType


class TopMediaHTTPAdapter(BaseHTTPAdapter):
    _service: ServiceType = ServiceType.TOPMEDIA

    def __init__(
        self,
        # timeount: int = 60,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(
            service=self._service,
            *args,
            **kwargs,
        )
