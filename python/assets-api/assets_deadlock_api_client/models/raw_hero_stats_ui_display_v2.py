from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RawHeroStatsUIDisplayV2")


@_attrs_define
class RawHeroStatsUIDisplayV2:
    """
    Attributes:
        category (str):
        stat_type (str):
    """

    category: str
    stat_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        stat_type = self.stat_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "stat_type": stat_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        stat_type = d.pop("stat_type")

        raw_hero_stats_ui_display_v2 = cls(
            category=category,
            stat_type=stat_type,
        )

        raw_hero_stats_ui_display_v2.additional_properties = d
        return raw_hero_stats_ui_display_v2

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
