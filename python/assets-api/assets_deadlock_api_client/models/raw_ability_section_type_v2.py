from enum import Enum


class RawAbilitySectionTypeV2(str, Enum):
    ACTIVE = "active"
    INNATE = "innate"
    PASSIVE = "passive"

    def __str__(self) -> str:
        return str(self.value)
