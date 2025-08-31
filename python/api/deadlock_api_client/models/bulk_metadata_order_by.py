from enum import Enum


class BulkMetadataOrderBy(str, Enum):
    MATCH_ID = "match_id"
    START_TIME = "start_time"

    def __str__(self) -> str:
        return str(self.value)
