from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RawHeroPurchaseBonusV2")


@_attrs_define
class RawHeroPurchaseBonusV2:
    """
    Attributes:
        value_type (str):
        tier (int):
        value (str):
    """

    value_type: str
    tier: int
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_type = self.value_type

        tier = self.tier

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value_type": value_type,
                "tier": tier,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value_type = d.pop("value_type")

        tier = d.pop("tier")

        value = d.pop("value")

        raw_hero_purchase_bonus_v2 = cls(
            value_type=value_type,
            tier=tier,
            value=value,
        )

        raw_hero_purchase_bonus_v2.additional_properties = d
        return raw_hero_purchase_bonus_v2

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
