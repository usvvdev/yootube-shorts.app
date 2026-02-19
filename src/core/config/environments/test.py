# coding utf-8

# packages

from logging import DEBUG

# application dependencies

from ..base import ApplicationBaseConfig

from src.domain.types.enums.common import AppMode


class ApplicationTestConfig(ApplicationBaseConfig):
    mode: AppMode = AppMode.TEST

    logging_level: int = DEBUG
