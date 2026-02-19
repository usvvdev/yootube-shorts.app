# coding utf-8

# packages

from pydantic import Field

# application dependencies

from ..common import BaseModelType


class TelegramOptions(BaseModelType):
    bot_token: str | None = Field(
        default=None,
        description="Telegram bot API token used for authentication.",
    )

    chat_id: int | None = Field(
        default=None,
        description="Telegram chat ID where messages will be sent.",
    )
