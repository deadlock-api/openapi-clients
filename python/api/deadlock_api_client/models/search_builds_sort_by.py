from enum import Enum


class SearchBuildsSortBy(str, Enum):
    FAVORITES = "favorites"
    IGNORES = "ignores"
    PUBLISHED_AT = "published_at"
    REPORTS = "reports"
    UPDATED_AT = "updated_at"
    VERSION = "version"
    WEEKLY_FAVORITES = "weekly_favorites"

    def __str__(self) -> str:
        return str(self.value)
