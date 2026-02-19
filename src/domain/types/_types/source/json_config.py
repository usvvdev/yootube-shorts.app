# coding utf-8

from typing import Any

from json import (
    load,
    JSONDecodeError,
)

from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    JsonConfigSettingsSource,
)


class EnvironmentJsonConfigSettingsSource(JsonConfigSettingsSource):
    def __init__(
        self,
        settings_cls: type[BaseSettings],
        json_file: Path,
        mode: str,
    ) -> None:
        self._json_file: Path = json_file
        self._mode: str = mode

        super().__init__(
            settings_cls,
            json_file,
        )

    def __call__(self) -> dict[str, Any]:
        if not self._json_file.exists():
            return {}

        try:
            with self._json_file.open("r", encoding="utf-8") as f:
                data: dict[str, Any] = load(f)
        except (JSONDecodeError, OSError):
            return {}

        common = data.get("common", {})

        mode_data = data.get(self._mode, {})

        return self.__merge_data(common, mode_data)

    @staticmethod
    def __merge_data(
        base_config: dict[str, Any],
        override_config: dict[str, Any],
    ) -> dict[str, Any]:
        result: dict[str, Any] = base_config.copy()
        for key, value in override_config.items():
            config_value = result.get(key)
            if isinstance(config_value, dict) and isinstance(value, dict):
                result[key] = __class__.__merge_data(
                    config_value,
                    value,
                )
            else:
                result[key] = value
        return result
