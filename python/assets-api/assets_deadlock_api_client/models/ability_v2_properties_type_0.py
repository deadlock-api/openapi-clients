from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.item_property_v2 import ItemPropertyV2


T = TypeVar("T", bound="AbilityV2PropertiesType0")


@_attrs_define
class AbilityV2PropertiesType0:
    """ """

    additional_properties: dict[str, "ItemPropertyV2"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item_property_v2 import ItemPropertyV2

        d = dict(src_dict)
        ability_v2_properties_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ItemPropertyV2.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        ability_v2_properties_type_0.additional_properties = additional_properties
        return ability_v2_properties_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "ItemPropertyV2":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "ItemPropertyV2") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
