from enum import Enum


class ActiveMatchGameMode(str, Enum):
    KECITADELGAMEMODE1V1TEST = "KECitadelGameMode1v1Test"
    KECITADELGAMEMODEINVALID = "KECitadelGameModeInvalid"
    KECITADELGAMEMODENORMAL = "KECitadelGameModeNormal"
    KECITADELGAMEMODESANDBOX = "KECitadelGameModeSandbox"

    def __str__(self) -> str:
        return str(self.value)
