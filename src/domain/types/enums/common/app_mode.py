# coding utf-8

from enum import StrEnum


class AppMode(StrEnum):
    PRODUCTION = "production"

    DEVELOPMENT = "development"

    TEST = "test"
