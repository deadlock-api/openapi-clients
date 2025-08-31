from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.raw_ability_upgrade_property_upgrade_v2 import RawAbilityUpgradePropertyUpgradeV2


T = TypeVar("T", bound="RawAbilityUpgradeV2")


@_attrs_define
class RawAbilityUpgradeV2:
    """
    Attributes:
        property_upgrades (Union[Unset, list['RawAbilityUpgradePropertyUpgradeV2']]):
    """

    property_upgrades: Union[Unset, list["RawAbilityUpgradePropertyUpgradeV2"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_upgrades: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.property_upgrades, Unset):
            property_upgrades = []
            for property_upgrades_item_data in self.property_upgrades:
                property_upgrades_item = property_upgrades_item_data.to_dict()
                property_upgrades.append(property_upgrades_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_upgrades is not UNSET:
            field_dict["property_upgrades"] = property_upgrades

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_ability_upgrade_property_upgrade_v2 import RawAbilityUpgradePropertyUpgradeV2

        d = dict(src_dict)
        property_upgrades = []
        _property_upgrades = d.pop("property_upgrades", UNSET)
        for property_upgrades_item_data in _property_upgrades or []:
            property_upgrades_item = RawAbilityUpgradePropertyUpgradeV2.from_dict(property_upgrades_item_data)

            property_upgrades.append(property_upgrades_item)

        raw_ability_upgrade_v2 = cls(
            property_upgrades=property_upgrades,
        )

        raw_ability_upgrade_v2.additional_properties = d
        return raw_ability_upgrade_v2

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
