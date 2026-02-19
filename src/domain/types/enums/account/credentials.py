# coding utf-8

from enum import StrEnum


class AccountCredentialsType(StrEnum):
    ACCESS_KEY = "ACCESS_KEY"

    SECRET_KEY = "SECRET_KEY"

    API_KEY = "API_KEY"

    OAUTH_TOKEN = "OAUTH_TOKEN"

    COOKIES = "COOKIES"

    USER_ID = "USER_ID"

    GOOGLE_CREDENTIALS = "GOOGLE_CREDENTIALS"


class AccountCredentialStorageType(StrEnum):
    INLINE = "INLINE"

    OBJECT = "OBJECT"


__all__: list[str] = [
    "AccountCredentialsType",
    "AccountCredentialStorageType",
]
