from enum import Enum


class CommandResolveRegion(str, Enum):
    ASIA = "Asia"
    EUROPE = "Europe"
    NAMERICA = "NAmerica"
    OCEANIA = "Oceania"
    SAMERICA = "SAmerica"

    def __str__(self) -> str:
        return str(self.value)
