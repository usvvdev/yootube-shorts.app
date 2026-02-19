# coding utf-8

from enum import StrEnum


class UserGenerationStatus(StrEnum):
    PENDING = "PENDING"

    SUCCESS = "SUCCESS"

    FAILED = "FAILED"

    UPLOADING = "UPLOADING"
