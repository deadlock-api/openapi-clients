from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ColorV1")


@_attrs_define
class ColorV1:
    """
    Attributes:
        red (int): The red value of the color.
        green (int): The green value of the color.
        blue (int): The blue value of the color.
        alpha (int): The alpha value of the color.
    """

    red: int
    green: int
    blue: int
    alpha: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        red = self.red

        green = self.green

        blue = self.blue

        alpha = self.alpha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "red": red,
                "green": green,
                "blue": blue,
                "alpha": alpha,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        red = d.pop("red")

        green = d.pop("green")

        blue = d.pop("blue")

        alpha = d.pop("alpha")

        color_v1 = cls(
            red=red,
            green=green,
            blue=blue,
            alpha=alpha,
        )

        color_v1.additional_properties = d
        return color_v1

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
