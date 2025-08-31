from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BuildTagV2")


@_attrs_define
class BuildTagV2:
    """
    Attributes:
        class_name (str):
        label (str):
        id (int):
        icon (str):
    """

    class_name: str
    label: str
    id: int
    icon: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_name = self.class_name

        label = self.label

        id = self.id

        icon = self.icon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "class_name": class_name,
                "label": label,
                "id": id,
                "icon": icon,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        class_name = d.pop("class_name")

        label = d.pop("label")

        id = d.pop("id")

        icon = d.pop("icon")

        build_tag_v2 = cls(
            class_name=class_name,
            label=label,
            id=id,
            icon=icon,
        )

        build_tag_v2.additional_properties = d
        return build_tag_v2

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
