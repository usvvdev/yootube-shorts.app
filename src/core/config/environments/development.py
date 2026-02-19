# coding utf-8

# packages

from logging import DEBUG

# application dependencies

from ..base import ApplicationBaseConfig

from src.domain.types.enums.common import AppMode


class ApplicationDevConfig(ApplicationBaseConfig):
    mode: AppMode = AppMode.DEVELOPMENT

    logging_level: int = DEBUG
