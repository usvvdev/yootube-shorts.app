# coding utf-8

# application depencies

from ....common.http import BaseHTTPAdapter

from src.domain.types.enums.common import ServiceType


class PixverseHTTPAdapter(BaseHTTPAdapter):
    _service: ServiceType = ServiceType.PIXVERSE

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
