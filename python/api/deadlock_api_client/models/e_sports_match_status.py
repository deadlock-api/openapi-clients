from enum import Enum


class ESportsMatchStatus(str, Enum):
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"
    LIVE = "Live"
    SCHEDULED = "Scheduled"

    def __str__(self) -> str:
        return str(self.value)
