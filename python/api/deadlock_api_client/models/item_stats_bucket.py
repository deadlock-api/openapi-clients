from enum import Enum


class ItemStatsBucket(str, Enum):
    GAME_TIME_MIN = "game_time_min"
    GAME_TIME_NORMALIZED_PERCENTAGE = "game_time_normalized_percentage"
    HERO = "hero"
    NET_WORTH_BY_1000 = "net_worth_by_1000"
    NET_WORTH_BY_10000 = "net_worth_by_10000"
    NET_WORTH_BY_2000 = "net_worth_by_2000"
    NET_WORTH_BY_3000 = "net_worth_by_3000"
    NET_WORTH_BY_5000 = "net_worth_by_5000"
    NO_BUCKET = "no_bucket"
    START_TIME_DAY = "start_time_day"
    START_TIME_HOUR = "start_time_hour"
    START_TIME_MONTH = "start_time_month"
    START_TIME_WEEK = "start_time_week"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
