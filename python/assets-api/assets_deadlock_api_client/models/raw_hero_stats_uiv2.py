from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.raw_hero_stats_ui_display_v2 import RawHeroStatsUIDisplayV2


T = TypeVar("T", bound="RawHeroStatsUIV2")


@_attrs_define
class RawHeroStatsUIV2:
    """
    Attributes:
        weapon_stat_display (str):
        display_stats (list['RawHeroStatsUIDisplayV2']):
    """

    weapon_stat_display: str
    display_stats: list["RawHeroStatsUIDisplayV2"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weapon_stat_display = self.weapon_stat_display

        display_stats = []
        for display_stats_item_data in self.display_stats:
            display_stats_item = display_stats_item_data.to_dict()
            display_stats.append(display_stats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "weapon_stat_display": weapon_stat_display,
                "display_stats": display_stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_hero_stats_ui_display_v2 import RawHeroStatsUIDisplayV2

        d = dict(src_dict)
        weapon_stat_display = d.pop("weapon_stat_display")

        display_stats = []
        _display_stats = d.pop("display_stats")
        for display_stats_item_data in _display_stats:
            display_stats_item = RawHeroStatsUIDisplayV2.from_dict(display_stats_item_data)

            display_stats.append(display_stats_item)

        raw_hero_stats_uiv2 = cls(
            weapon_stat_display=weapon_stat_display,
            display_stats=display_stats,
        )

        raw_hero_stats_uiv2.additional_properties = d
        return raw_hero_stats_uiv2

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
