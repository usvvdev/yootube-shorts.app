# coding utf-8

# application depencies

from ....common.http import BaseHTTPAdapter


class PixverseClient(BaseHTTPAdapter):
    def __init__(
        self,
        timeount: int = 60,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(
            timeount=timeount,
            *args,
            **kwargs,
        )
