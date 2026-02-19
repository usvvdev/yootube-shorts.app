# coding utf-8

from enum import StrEnum


class RequestMethod(StrEnum):
    GET = "get"

    POST = "post"

    PUT = "put"

    UPDATE = "update"

    DELETE = "delete"
