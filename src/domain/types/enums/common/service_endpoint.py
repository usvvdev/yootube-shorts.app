# coding utf-8

from enum import StrEnum


class ServiceEndpoint(StrEnum):
    BASE = "base"

    AUTHORIZATION = "authorization"

    VOICE = "voice"
