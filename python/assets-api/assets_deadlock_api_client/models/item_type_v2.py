from enum import Enum


class ItemTypeV2(str, Enum):
    ABILITY = "ability"
    ARMOR = "armor"
    TECH = "tech"
    UPGRADE = "upgrade"
    WEAPON = "weapon"

    def __str__(self) -> str:
        return str(self.value)
