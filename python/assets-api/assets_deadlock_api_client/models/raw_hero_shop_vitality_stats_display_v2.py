from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RawHeroShopVitalityStatsDisplayV2")


@_attrs_define
class RawHeroShopVitalityStatsDisplayV2:
    """
    Attributes:
        display_stats (list[str]):
        other_display_stats (list[str]):
    """

    display_stats: list[str]
    other_display_stats: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_stats = self.display_stats

        other_display_stats = self.other_display_stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display_stats": display_stats,
                "other_display_stats": other_display_stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_stats = cast(list[str], d.pop("display_stats"))

        other_display_stats = cast(list[str], d.pop("other_display_stats"))

        raw_hero_shop_vitality_stats_display_v2 = cls(
            display_stats=display_stats,
            other_display_stats=other_display_stats,
        )

        raw_hero_shop_vitality_stats_display_v2.additional_properties = d
        return raw_hero_shop_vitality_stats_display_v2

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
