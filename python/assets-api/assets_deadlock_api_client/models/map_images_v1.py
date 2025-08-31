from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MapImagesV1")


@_attrs_define
class MapImagesV1:
    """
    Attributes:
        minimap (str): The minimap image of the map.
        plain (str): The minimap image of the map without background image and frame image.
        background (str): The background image of the map.
        frame (str): The frame image of the map.
        mid (str): The mid image of the map.
    """

    minimap: str
    plain: str
    background: str
    frame: str
    mid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        minimap = self.minimap

        plain = self.plain

        background = self.background

        frame = self.frame

        mid = self.mid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "minimap": minimap,
                "plain": plain,
                "background": background,
                "frame": frame,
                "mid": mid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        minimap = d.pop("minimap")

        plain = d.pop("plain")

        background = d.pop("background")

        frame = d.pop("frame")

        mid = d.pop("mid")

        map_images_v1 = cls(
            minimap=minimap,
            plain=plain,
            background=background,
            frame=frame,
            mid=mid,
        )

        map_images_v1.additional_properties = d
        return map_images_v1

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
