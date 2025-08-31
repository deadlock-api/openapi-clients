from enum import Enum


class HeroItemTypeV2(str, Enum):
    ABILITY_CLIMB_ROPE = "ability_climb_rope"
    ABILITY_INNATE1 = "ability_innate1"
    ABILITY_INNATE2 = "ability_innate2"
    ABILITY_INNATE3 = "ability_innate3"
    ABILITY_JUMP = "ability_jump"
    ABILITY_MANTLE = "ability_mantle"
    ABILITY_SLIDE = "ability_slide"
    ABILITY_ZIP_LINE = "ability_zip_line"
    ABILITY_ZIP_LINE_BOOST = "ability_zip_line_boost"
    SIGNATURE1 = "signature1"
    SIGNATURE2 = "signature2"
    SIGNATURE3 = "signature3"
    SIGNATURE4 = "signature4"
    WEAPON_MELEE = "weapon_melee"
    WEAPON_PRIMARY = "weapon_primary"
    WEAPON_SECONDARY = "weapon_secondary"

    def __str__(self) -> str:
        return str(self.value)
