from enum import Enum


class RawAbilityActivationV2(str, Enum):
    HOLD_TOGGLE = "hold_toggle"
    INSTANT_CAST = "instant_cast"
    ON_BUTTON_IS_DOWN = "on_button_is_down"
    PASSIVE = "passive"
    PRESS = "press"
    PRESS_TOGGLE = "press_toggle"

    def __str__(self) -> str:
        return str(self.value)
