from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ability_tooltip_details_info_section_v2 import AbilityTooltipDetailsInfoSectionV2


T = TypeVar("T", bound="AbilityTooltipDetailsV2")


@_attrs_define
class AbilityTooltipDetailsV2:
    """
    Attributes:
        info_sections (Union[None, Unset, list['AbilityTooltipDetailsInfoSectionV2']]):
        additional_header_properties (Union[None, Unset, list[str]]):
    """

    info_sections: Union[None, Unset, list["AbilityTooltipDetailsInfoSectionV2"]] = UNSET
    additional_header_properties: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        info_sections: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.info_sections, Unset):
            info_sections = UNSET
        elif isinstance(self.info_sections, list):
            info_sections = []
            for info_sections_type_0_item_data in self.info_sections:
                info_sections_type_0_item = info_sections_type_0_item_data.to_dict()
                info_sections.append(info_sections_type_0_item)

        else:
            info_sections = self.info_sections

        additional_header_properties: Union[None, Unset, list[str]]
        if isinstance(self.additional_header_properties, Unset):
            additional_header_properties = UNSET
        elif isinstance(self.additional_header_properties, list):
            additional_header_properties = self.additional_header_properties

        else:
            additional_header_properties = self.additional_header_properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if info_sections is not UNSET:
            field_dict["info_sections"] = info_sections
        if additional_header_properties is not UNSET:
            field_dict["additional_header_properties"] = additional_header_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ability_tooltip_details_info_section_v2 import AbilityTooltipDetailsInfoSectionV2

        d = dict(src_dict)

        def _parse_info_sections(data: object) -> Union[None, Unset, list["AbilityTooltipDetailsInfoSectionV2"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                info_sections_type_0 = []
                _info_sections_type_0 = data
                for info_sections_type_0_item_data in _info_sections_type_0:
                    info_sections_type_0_item = AbilityTooltipDetailsInfoSectionV2.from_dict(
                        info_sections_type_0_item_data
                    )

                    info_sections_type_0.append(info_sections_type_0_item)

                return info_sections_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AbilityTooltipDetailsInfoSectionV2"]], data)

        info_sections = _parse_info_sections(d.pop("info_sections", UNSET))

        def _parse_additional_header_properties(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                additional_header_properties_type_0 = cast(list[str], data)

                return additional_header_properties_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        additional_header_properties = _parse_additional_header_properties(d.pop("additional_header_properties", UNSET))

        ability_tooltip_details_v2 = cls(
            info_sections=info_sections,
            additional_header_properties=additional_header_properties,
        )

        ability_tooltip_details_v2.additional_properties = d
        return ability_tooltip_details_v2

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
