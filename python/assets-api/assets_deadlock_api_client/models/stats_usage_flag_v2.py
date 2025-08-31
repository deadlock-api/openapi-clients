from enum import Enum


class StatsUsageFlagV2(str, Enum):
    CONDITIONALLYAPPLIED = "ConditionallyApplied"
    CONDITIONALLYENEMYAPPLIED = "ConditionallyEnemyApplied"
    INTRINSICALLYPROVIDEDINABILITY = "IntrinsicallyProvidedInAbility"
    INTRINSICALLYPROVIDEDINMODIFIER = "IntrinsicallyProvidedInModifier"

    def __str__(self) -> str:
        return str(self.value)
