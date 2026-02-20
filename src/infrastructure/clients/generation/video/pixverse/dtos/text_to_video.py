# coding utf-8

# packages

from pydantic import Field

# application depencies

from src.domain.types._types.common import BaseModelType


class T2VDTO(BaseModelType):
    prompt: str = Field(
        ...,
        description="",
    )

    duration: int = Field(
        default=10,
        description="",
    )

    quality: str = Field(
        default="720p",
        description="",
    )

    motion_mode: str = Field(
        default="normal",
        description="",
    )

    model: str = Field(
        default="v4.5",
        description="",
    )

    lip_sync_tts_speaker_id: str = Field(
        default="Auto",
        description="",
    )

    aspect_ratio: str = Field(
        default="9:16",
        description="",
    )
