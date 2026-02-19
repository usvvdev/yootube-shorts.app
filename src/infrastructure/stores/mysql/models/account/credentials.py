# coding utf-8

from typing import ClassVar

from sqlalchemy import (
    Integer,
    Text,
    Enum,
    String,
    ForeignKey,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

# application dependencies

from ..common import (
    BaseMixin,
    TimestampMixin,
)

from src.domain.types.enums.account import (
    AccountCredentialsType,
    AccountCredentialStorageType,
)


class AccountCredentials(
    BaseMixin,
    TimestampMixin,
):
    type: Mapped[AccountCredentialsType] = mapped_column(
        Enum(
            AccountCredentialsType,
            native_enum=False,
        ),
        default=AccountCredentialsType.GOOGLE_CREDENTIALS,
        nullable=False,
    )

    storage: Mapped[AccountCredentialStorageType] = mapped_column(
        Enum(
            AccountCredentialStorageType,
            native_enum=False,
        ),
        default=AccountCredentialStorageType.OBJECT,
        nullable=False,
    )

    value: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    object_key: Mapped[str] = mapped_column(
        String(512),
        nullable=True,
    )

    account_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "accounts.id",
            ondelete="CASCADE",
        ),
        index=True,
        nullable=False,
    )

    __updated_at__: ClassVar[bool] = True
