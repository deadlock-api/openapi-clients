from enum import Enum


class HeroTypeV2(str, Enum):
    ASSASSIN = "assassin"
    BRAWLER = "brawler"
    MARKSMAN = "marksman"
    MYSTIC = "mystic"

    def __str__(self) -> str:
        return str(self.value)
