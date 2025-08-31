from enum import Enum


class ActiveMatchMode(str, Enum):
    COOPBOT = "CoopBot"
    HEROLABS = "HeroLabs"
    INVALID = "Invalid"
    PRIVATELOBBY = "PrivateLobby"
    RANKED = "Ranked"
    SERVERTEST = "ServerTest"
    TUTORIAL = "Tutorial"
    UNRANKED = "Unranked"

    def __str__(self) -> str:
        return str(self.value)
