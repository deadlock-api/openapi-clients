from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RawHeroStatsDisplayV2")


@_attrs_define
class RawHeroStatsDisplayV2:
    """
    Attributes:
        health_header_stats (list[str]):
        health_stats (list[str]):
        magic_header_stats (list[str]):
        magic_stats (list[str]):
        weapon_header_stats (list[str]):
        weapon_stats (list[str]):
    """

    health_header_stats: list[str]
    health_stats: list[str]
    magic_header_stats: list[str]
    magic_stats: list[str]
    weapon_header_stats: list[str]
    weapon_stats: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        health_header_stats = self.health_header_stats

        health_stats = self.health_stats

        magic_header_stats = self.magic_header_stats

        magic_stats = self.magic_stats

        weapon_header_stats = self.weapon_header_stats

        weapon_stats = self.weapon_stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "health_header_stats": health_header_stats,
                "health_stats": health_stats,
                "magic_header_stats": magic_header_stats,
                "magic_stats": magic_stats,
                "weapon_header_stats": weapon_header_stats,
                "weapon_stats": weapon_stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        health_header_stats = cast(list[str], d.pop("health_header_stats"))

        health_stats = cast(list[str], d.pop("health_stats"))

        magic_header_stats = cast(list[str], d.pop("magic_header_stats"))

        magic_stats = cast(list[str], d.pop("magic_stats"))

        weapon_header_stats = cast(list[str], d.pop("weapon_header_stats"))

        weapon_stats = cast(list[str], d.pop("weapon_stats"))

        raw_hero_stats_display_v2 = cls(
            health_header_stats=health_header_stats,
            health_stats=health_stats,
            magic_header_stats=magic_header_stats,
            magic_stats=magic_stats,
            weapon_header_stats=weapon_header_stats,
            weapon_stats=weapon_stats,
        )

        raw_hero_stats_display_v2.additional_properties = d
        return raw_hero_stats_display_v2

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
