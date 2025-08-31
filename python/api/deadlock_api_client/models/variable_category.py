from enum import Enum


class VariableCategory(str, Enum):
    DAILY = "Daily"
    GENERAL = "General"
    HERO = "Hero"
    LEADERBOARD = "Leaderboard"
    OVERALL = "Overall"

    def __str__(self) -> str:
        return str(self.value)
