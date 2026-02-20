# coding utf-8

from enum import StrEnum


class ServiceEndpoint(StrEnum):
    BASE = "base"

    AUTHORIZATION = "authorization"

    VOICE = "voice"

    T2V = "t2v"
