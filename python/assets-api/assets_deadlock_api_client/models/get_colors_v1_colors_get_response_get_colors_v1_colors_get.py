from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.color_v1 import ColorV1


T = TypeVar("T", bound="GetColorsV1ColorsGetResponseGetColorsV1ColorsGet")


@_attrs_define
class GetColorsV1ColorsGetResponseGetColorsV1ColorsGet:
    """ """

    additional_properties: dict[str, "ColorV1"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color_v1 import ColorV1

        d = dict(src_dict)
        get_colors_v1_colors_get_response_get_colors_v1_colors_get = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ColorV1.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_colors_v1_colors_get_response_get_colors_v1_colors_get.additional_properties = additional_properties
        return get_colors_v1_colors_get_response_get_colors_v1_colors_get

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "ColorV1":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "ColorV1") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
