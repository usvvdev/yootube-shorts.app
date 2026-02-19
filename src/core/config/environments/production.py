# coding utf-8

from ..base import ApplicationBaseConfig

from src.domain.types.enums.common import AppMode


class ApplicationProdConfig(ApplicationBaseConfig):
    mode: AppMode = AppMode.PRODUCTION
