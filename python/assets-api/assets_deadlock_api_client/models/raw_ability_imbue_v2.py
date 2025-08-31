from enum import Enum


class RawAbilityImbueV2(str, Enum):
    IMBUE_ACTIVE = "imbue_active"
    IMBUE_ACTIVE_NON_ULT = "imbue_active_non_ult"
    IMBUE_MODIFIER_VALUE = "imbue_modifier_value"

    def __str__(self) -> str:
        return str(self.value)
