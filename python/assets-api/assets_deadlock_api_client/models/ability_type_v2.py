from enum import Enum


class AbilityTypeV2(str, Enum):
    INNATE = "innate"
    ITEM = "item"
    MELEE = "melee"
    SIGNATURE = "signature"
    ULTIMATE = "ultimate"
    WEAPON = "weapon"

    def __str__(self) -> str:
        return str(self.value)
