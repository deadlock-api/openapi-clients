from enum import Enum


class HeroStatsBucket(str, Enum):
    NO_BUCKET = "no_bucket"
    START_TIME_DAY = "start_time_day"
    START_TIME_HOUR = "start_time_hour"
    START_TIME_MONTH = "start_time_month"
    START_TIME_WEEK = "start_time_week"

    def __str__(self) -> str:
        return str(self.value)
