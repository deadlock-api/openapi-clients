from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.upgrade_tooltip_section_attribute_v2_important_property_with_icon import (
        UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon,
    )


T = TypeVar("T", bound="UpgradeTooltipSectionAttributeV2")


@_attrs_define
class UpgradeTooltipSectionAttributeV2:
    """
    Attributes:
        loc_string (Union[None, Unset, str]):
        properties (Union[None, Unset, list[str]]):
        elevated_properties (Union[None, Unset, list[str]]):
        important_properties (Union[None, Unset, list[str]]):
        important_properties_with_icon (Union[None, Unset,
            list['UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon']]):
    """

    loc_string: Union[None, Unset, str] = UNSET
    properties: Union[None, Unset, list[str]] = UNSET
    elevated_properties: Union[None, Unset, list[str]] = UNSET
    important_properties: Union[None, Unset, list[str]] = UNSET
    important_properties_with_icon: Union[
        None, Unset, list["UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        loc_string: Union[None, Unset, str]
        if isinstance(self.loc_string, Unset):
            loc_string = UNSET
        else:
            loc_string = self.loc_string

        properties: Union[None, Unset, list[str]]
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif isinstance(self.properties, list):
            properties = self.properties

        else:
            properties = self.properties

        elevated_properties: Union[None, Unset, list[str]]
        if isinstance(self.elevated_properties, Unset):
            elevated_properties = UNSET
        elif isinstance(self.elevated_properties, list):
            elevated_properties = self.elevated_properties

        else:
            elevated_properties = self.elevated_properties

        important_properties: Union[None, Unset, list[str]]
        if isinstance(self.important_properties, Unset):
            important_properties = UNSET
        elif isinstance(self.important_properties, list):
            important_properties = self.important_properties

        else:
            important_properties = self.important_properties

        important_properties_with_icon: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.important_properties_with_icon, Unset):
            important_properties_with_icon = UNSET
        elif isinstance(self.important_properties_with_icon, list):
            important_properties_with_icon = []
            for important_properties_with_icon_type_0_item_data in self.important_properties_with_icon:
                important_properties_with_icon_type_0_item = important_properties_with_icon_type_0_item_data.to_dict()
                important_properties_with_icon.append(important_properties_with_icon_type_0_item)

        else:
            important_properties_with_icon = self.important_properties_with_icon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loc_string is not UNSET:
            field_dict["loc_string"] = loc_string
        if properties is not UNSET:
            field_dict["properties"] = properties
        if elevated_properties is not UNSET:
            field_dict["elevated_properties"] = elevated_properties
        if important_properties is not UNSET:
            field_dict["important_properties"] = important_properties
        if important_properties_with_icon is not UNSET:
            field_dict["important_properties_with_icon"] = important_properties_with_icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upgrade_tooltip_section_attribute_v2_important_property_with_icon import (
            UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon,
        )

        d = dict(src_dict)

        def _parse_loc_string(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        loc_string = _parse_loc_string(d.pop("loc_string", UNSET))

        def _parse_properties(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                properties_type_0 = cast(list[str], data)

                return properties_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        properties = _parse_properties(d.pop("properties", UNSET))

        def _parse_elevated_properties(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                elevated_properties_type_0 = cast(list[str], data)

                return elevated_properties_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        elevated_properties = _parse_elevated_properties(d.pop("elevated_properties", UNSET))

        def _parse_important_properties(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                important_properties_type_0 = cast(list[str], data)

                return important_properties_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        important_properties = _parse_important_properties(d.pop("important_properties", UNSET))

        def _parse_important_properties_with_icon(
            data: object,
        ) -> Union[None, Unset, list["UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                important_properties_with_icon_type_0 = []
                _important_properties_with_icon_type_0 = data
                for important_properties_with_icon_type_0_item_data in _important_properties_with_icon_type_0:
                    important_properties_with_icon_type_0_item = (
                        UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon.from_dict(
                            important_properties_with_icon_type_0_item_data
                        )
                    )

                    important_properties_with_icon_type_0.append(important_properties_with_icon_type_0_item)

                return important_properties_with_icon_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon"]], data)

        important_properties_with_icon = _parse_important_properties_with_icon(
            d.pop("important_properties_with_icon", UNSET)
        )

        upgrade_tooltip_section_attribute_v2 = cls(
            loc_string=loc_string,
            properties=properties,
            elevated_properties=elevated_properties,
            important_properties=important_properties,
            important_properties_with_icon=important_properties_with_icon,
        )

        upgrade_tooltip_section_attribute_v2.additional_properties = d
        return upgrade_tooltip_section_attribute_v2

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
