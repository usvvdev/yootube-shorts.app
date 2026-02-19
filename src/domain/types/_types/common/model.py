# coding utf-8

from typing import Any

from pydantic import (
    BaseModel,
    ConfigDict,
)


class BaseModelType(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        use_enum_values=True,
        loc_by_alias=True,
        from_attributes=True,
        arbitrary_types_allowed=True,
    )

    @property
    def dump(
        self,
    ) -> dict[str, Any]:
        return self.model_dump(
            by_alias=True,
            exclude_none=True,
            mode="json",
        )
