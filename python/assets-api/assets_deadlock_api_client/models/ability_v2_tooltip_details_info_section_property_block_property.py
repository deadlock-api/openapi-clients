from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty")


@_attrs_define
class AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty:
    """
    Attributes:
        requires_ability_upgrade (Union[None, Unset, bool]):
        show_property_value (Union[None, Unset, bool]):
        important_property (Union[None, Unset, str]):
        status_effect_value (Union[None, Unset, str]):
        status_effect_name (Union[None, Unset, str]):
        important_property_icon (Union[None, Unset, str]):
    """

    requires_ability_upgrade: Union[None, Unset, bool] = UNSET
    show_property_value: Union[None, Unset, bool] = UNSET
    important_property: Union[None, Unset, str] = UNSET
    status_effect_value: Union[None, Unset, str] = UNSET
    status_effect_name: Union[None, Unset, str] = UNSET
    important_property_icon: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requires_ability_upgrade: Union[None, Unset, bool]
        if isinstance(self.requires_ability_upgrade, Unset):
            requires_ability_upgrade = UNSET
        else:
            requires_ability_upgrade = self.requires_ability_upgrade

        show_property_value: Union[None, Unset, bool]
        if isinstance(self.show_property_value, Unset):
            show_property_value = UNSET
        else:
            show_property_value = self.show_property_value

        important_property: Union[None, Unset, str]
        if isinstance(self.important_property, Unset):
            important_property = UNSET
        else:
            important_property = self.important_property

        status_effect_value: Union[None, Unset, str]
        if isinstance(self.status_effect_value, Unset):
            status_effect_value = UNSET
        else:
            status_effect_value = self.status_effect_value

        status_effect_name: Union[None, Unset, str]
        if isinstance(self.status_effect_name, Unset):
            status_effect_name = UNSET
        else:
            status_effect_name = self.status_effect_name

        important_property_icon: Union[None, Unset, str]
        if isinstance(self.important_property_icon, Unset):
            important_property_icon = UNSET
        else:
            important_property_icon = self.important_property_icon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requires_ability_upgrade is not UNSET:
            field_dict["requires_ability_upgrade"] = requires_ability_upgrade
        if show_property_value is not UNSET:
            field_dict["show_property_value"] = show_property_value
        if important_property is not UNSET:
            field_dict["important_property"] = important_property
        if status_effect_value is not UNSET:
            field_dict["status_effect_value"] = status_effect_value
        if status_effect_name is not UNSET:
            field_dict["status_effect_name"] = status_effect_name
        if important_property_icon is not UNSET:
            field_dict["important_property_icon"] = important_property_icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_requires_ability_upgrade(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        requires_ability_upgrade = _parse_requires_ability_upgrade(d.pop("requires_ability_upgrade", UNSET))

        def _parse_show_property_value(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        show_property_value = _parse_show_property_value(d.pop("show_property_value", UNSET))

        def _parse_important_property(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        important_property = _parse_important_property(d.pop("important_property", UNSET))

        def _parse_status_effect_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status_effect_value = _parse_status_effect_value(d.pop("status_effect_value", UNSET))

        def _parse_status_effect_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status_effect_name = _parse_status_effect_name(d.pop("status_effect_name", UNSET))

        def _parse_important_property_icon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        important_property_icon = _parse_important_property_icon(d.pop("important_property_icon", UNSET))

        ability_v2_tooltip_details_info_section_property_block_property = cls(
            requires_ability_upgrade=requires_ability_upgrade,
            show_property_value=show_property_value,
            important_property=important_property,
            status_effect_value=status_effect_value,
            status_effect_name=status_effect_name,
            important_property_icon=important_property_icon,
        )

        ability_v2_tooltip_details_info_section_property_block_property.additional_properties = d
        return ability_v2_tooltip_details_info_section_property_block_property

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
