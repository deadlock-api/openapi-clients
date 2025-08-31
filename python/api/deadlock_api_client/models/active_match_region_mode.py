from enum import Enum


class ActiveMatchRegionMode(str, Enum):
    EUROPE = "Europe"
    OCEANIA = "Oceania"
    ROW = "Row"
    RUSSIA = "Russia"
    SAMERICA = "SAmerica"
    SEASIA = "SeAsia"

    def __str__(self) -> str:
        return str(self.value)
