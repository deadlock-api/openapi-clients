from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ability_tooltip_details_info_section_property_block_v2 import (
        AbilityTooltipDetailsInfoSectionPropertyBlockV2,
    )


T = TypeVar("T", bound="AbilityTooltipDetailsInfoSectionV2")


@_attrs_define
class AbilityTooltipDetailsInfoSectionV2:
    """
    Attributes:
        loc_string (Union[None, Unset, str]):
        property_upgrade_required (Union[None, Unset, str]):
        properties_block (Union[None, Unset, list['AbilityTooltipDetailsInfoSectionPropertyBlockV2']]):
        basic_properties (Union[None, Unset, list[str]]):
    """

    loc_string: Union[None, Unset, str] = UNSET
    property_upgrade_required: Union[None, Unset, str] = UNSET
    properties_block: Union[None, Unset, list["AbilityTooltipDetailsInfoSectionPropertyBlockV2"]] = UNSET
    basic_properties: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        loc_string: Union[None, Unset, str]
        if isinstance(self.loc_string, Unset):
            loc_string = UNSET
        else:
            loc_string = self.loc_string

        property_upgrade_required: Union[None, Unset, str]
        if isinstance(self.property_upgrade_required, Unset):
            property_upgrade_required = UNSET
        else:
            property_upgrade_required = self.property_upgrade_required

        properties_block: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.properties_block, Unset):
            properties_block = UNSET
        elif isinstance(self.properties_block, list):
            properties_block = []
            for properties_block_type_0_item_data in self.properties_block:
                properties_block_type_0_item = properties_block_type_0_item_data.to_dict()
                properties_block.append(properties_block_type_0_item)

        else:
            properties_block = self.properties_block

        basic_properties: Union[None, Unset, list[str]]
        if isinstance(self.basic_properties, Unset):
            basic_properties = UNSET
        elif isinstance(self.basic_properties, list):
            basic_properties = self.basic_properties

        else:
            basic_properties = self.basic_properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loc_string is not UNSET:
            field_dict["loc_string"] = loc_string
        if property_upgrade_required is not UNSET:
            field_dict["property_upgrade_required"] = property_upgrade_required
        if properties_block is not UNSET:
            field_dict["properties_block"] = properties_block
        if basic_properties is not UNSET:
            field_dict["basic_properties"] = basic_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ability_tooltip_details_info_section_property_block_v2 import (
            AbilityTooltipDetailsInfoSectionPropertyBlockV2,
        )

        d = dict(src_dict)

        def _parse_loc_string(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        loc_string = _parse_loc_string(d.pop("loc_string", UNSET))

        def _parse_property_upgrade_required(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_upgrade_required = _parse_property_upgrade_required(d.pop("property_upgrade_required", UNSET))

        def _parse_properties_block(
            data: object,
        ) -> Union[None, Unset, list["AbilityTooltipDetailsInfoSectionPropertyBlockV2"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                properties_block_type_0 = []
                _properties_block_type_0 = data
                for properties_block_type_0_item_data in _properties_block_type_0:
                    properties_block_type_0_item = AbilityTooltipDetailsInfoSectionPropertyBlockV2.from_dict(
                        properties_block_type_0_item_data
                    )

                    properties_block_type_0.append(properties_block_type_0_item)

                return properties_block_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AbilityTooltipDetailsInfoSectionPropertyBlockV2"]], data)

        properties_block = _parse_properties_block(d.pop("properties_block", UNSET))

        def _parse_basic_properties(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                basic_properties_type_0 = cast(list[str], data)

                return basic_properties_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        basic_properties = _parse_basic_properties(d.pop("basic_properties", UNSET))

        ability_tooltip_details_info_section_v2 = cls(
            loc_string=loc_string,
            property_upgrade_required=property_upgrade_required,
            properties_block=properties_block,
            basic_properties=basic_properties,
        )

        ability_tooltip_details_info_section_v2.additional_properties = d
        return ability_tooltip_details_info_section_v2

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
