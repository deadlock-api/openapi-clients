from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon")


@_attrs_define
class UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon:
    """
    Attributes:
        name (Union[None, Unset, str]):
        icon (Union[None, Unset, str]):
        localized_name (Union[None, Unset, str]):
    """

    name: Union[None, Unset, str] = UNSET
    icon: Union[None, Unset, str] = UNSET
    localized_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        icon: Union[None, Unset, str]
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        localized_name: Union[None, Unset, str]
        if isinstance(self.localized_name, Unset):
            localized_name = UNSET
        else:
            localized_name = self.localized_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if icon is not UNSET:
            field_dict["icon"] = icon
        if localized_name is not UNSET:
            field_dict["localized_name"] = localized_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_icon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_localized_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        localized_name = _parse_localized_name(d.pop("localized_name", UNSET))

        upgrade_tooltip_section_attribute_v2_important_property_with_icon = cls(
            name=name,
            icon=icon,
            localized_name=localized_name,
        )

        upgrade_tooltip_section_attribute_v2_important_property_with_icon.additional_properties = d
        return upgrade_tooltip_section_attribute_v2_important_property_with_icon

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
