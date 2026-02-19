# coding utf-8

# packages

from pydantic import Field

# application dependencies

from ..common import BaseModelType


class ServiceOptions(BaseModelType):
    timeout: int = Field(
        ...,
        description="Connection timeout for the service adapter",
    )
