from enum import Enum


class ItemSlotTypeV2(str, Enum):
    SPIRIT = "spirit"
    VITALITY = "vitality"
    WEAPON = "weapon"

    def __str__(self) -> str:
        return str(self.value)
