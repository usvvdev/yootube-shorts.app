# coding utf-8

from enum import StrEnum


class UserEventType(StrEnum):
    SUBSCRIPTION_STARTED = "subscription_started"

    SUBSCRIPTION_RENEWED = "subscription_renewed"

    NON_RENEWING_PURCHASE = "non_renewing_purchase"
