# coding utf-8

# packages

from pydantic import Field

# application dependencies

from ..common import (
    BaseModelType,
    BaseRootModelType,
)

from ...enums.common import ServiceType


class HostOptions(BaseRootModelType):
    root: dict[str, str | None]


class EndpointOptions(BaseModelType):
    host: str = Field(
        ...,
        description="",
    )

    path: str = Field(
        ...,
        description="",
    )

    def build(
        self,
        hosts: dict[str, str | None],
        *,
        path_params: dict[str, str | int] | None = None,
    ) -> str:
        base_url: str | None = hosts.get(self.host)
        if not base_url:
            raise KeyError(f"Host '{self.host}' not found")

        path = self.path.format(**(path_params or {}))

        return f"{base_url}{path}"


class ServiceURLOptions(BaseModelType):
    hosts: HostOptions = Field(
        ...,
        description="",
    )
    endpoints: dict[str, EndpointOptions] = Field(
        ...,
        description="",
    )

    def build_url(
        self,
        endpoint: str,
    ) -> str:
        return self.endpoints[endpoint].build(
            self.hosts.root,
        )


class ServiceOptions(BaseRootModelType):
    root: dict[str, ServiceURLOptions]

    def get_options(
        self,
        service: ServiceType,
    ) -> ServiceURLOptions:
        service_options: ServiceURLOptions | None = self.root.get(service)
        if not service_options:
            raise KeyError()

        return service_options
