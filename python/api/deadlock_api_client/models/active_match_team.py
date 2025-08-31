from enum import Enum


class ActiveMatchTeam(str, Enum):
    SPECTATOR = "Spectator"
    TEAM0 = "Team0"
    TEAM1 = "Team1"

    def __str__(self) -> str:
        return str(self.value)
