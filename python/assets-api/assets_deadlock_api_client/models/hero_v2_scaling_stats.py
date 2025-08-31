from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.raw_hero_scaling_stat_v2 import RawHeroScalingStatV2


T = TypeVar("T", bound="HeroV2ScalingStats")


@_attrs_define
class HeroV2ScalingStats:
    """ """

    additional_properties: dict[str, "RawHeroScalingStatV2"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_hero_scaling_stat_v2 import RawHeroScalingStatV2

        d = dict(src_dict)
        hero_v2_scaling_stats = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RawHeroScalingStatV2.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        hero_v2_scaling_stats.additional_properties = additional_properties
        return hero_v2_scaling_stats

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "RawHeroScalingStatV2":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "RawHeroScalingStatV2") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
