from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ability_v2_tooltip_details_info_section_property_block_property import (
        AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty,
    )


T = TypeVar("T", bound="AbilityTooltipDetailsInfoSectionPropertyBlockV2")


@_attrs_define
class AbilityTooltipDetailsInfoSectionPropertyBlockV2:
    """
    Attributes:
        loc_string (Union[None, Unset, str]):
        properties (Union[None, Unset, list['AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty']]):
    """

    loc_string: Union[None, Unset, str] = UNSET
    properties: Union[None, Unset, list["AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        loc_string: Union[None, Unset, str]
        if isinstance(self.loc_string, Unset):
            loc_string = UNSET
        else:
            loc_string = self.loc_string

        properties: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif isinstance(self.properties, list):
            properties = []
            for properties_type_0_item_data in self.properties:
                properties_type_0_item = properties_type_0_item_data.to_dict()
                properties.append(properties_type_0_item)

        else:
            properties = self.properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loc_string is not UNSET:
            field_dict["loc_string"] = loc_string
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ability_v2_tooltip_details_info_section_property_block_property import (
            AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty,
        )

        d = dict(src_dict)

        def _parse_loc_string(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        loc_string = _parse_loc_string(d.pop("loc_string", UNSET))

        def _parse_properties(
            data: object,
        ) -> Union[None, Unset, list["AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                properties_type_0 = []
                _properties_type_0 = data
                for properties_type_0_item_data in _properties_type_0:
                    properties_type_0_item = AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty.from_dict(
                        properties_type_0_item_data
                    )

                    properties_type_0.append(properties_type_0_item)

                return properties_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty"]], data)

        properties = _parse_properties(d.pop("properties", UNSET))

        ability_tooltip_details_info_section_property_block_v2 = cls(
            loc_string=loc_string,
            properties=properties,
        )

        ability_tooltip_details_info_section_property_block_v2.additional_properties = d
        return ability_tooltip_details_info_section_property_block_v2

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
