from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ObjectivePositionV1")


@_attrs_define
class ObjectivePositionV1:
    """
    Attributes:
        left_relative (float): The relative margin left of the map image.
        top_relative (float): The relative margin top of the map image.
    """

    left_relative: float
    top_relative: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        left_relative = self.left_relative

        top_relative = self.top_relative

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "left_relative": left_relative,
                "top_relative": top_relative,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        left_relative = d.pop("left_relative")

        top_relative = d.pop("top_relative")

        objective_position_v1 = cls(
            left_relative=left_relative,
            top_relative=top_relative,
        )

        objective_position_v1.additional_properties = d
        return objective_position_v1

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
