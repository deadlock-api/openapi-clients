from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AbilityVideosV2")


@_attrs_define
class AbilityVideosV2:
    """
    Attributes:
        webm (Union[None, Unset, str]):
        mp4 (Union[None, Unset, str]):
    """

    webm: Union[None, Unset, str] = UNSET
    mp4: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webm: Union[None, Unset, str]
        if isinstance(self.webm, Unset):
            webm = UNSET
        else:
            webm = self.webm

        mp4: Union[None, Unset, str]
        if isinstance(self.mp4, Unset):
            mp4 = UNSET
        else:
            mp4 = self.mp4

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webm is not UNSET:
            field_dict["webm"] = webm
        if mp4 is not UNSET:
            field_dict["mp4"] = mp4

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_webm(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        webm = _parse_webm(d.pop("webm", UNSET))

        def _parse_mp4(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mp4 = _parse_mp4(d.pop("mp4", UNSET))

        ability_videos_v2 = cls(
            webm=webm,
            mp4=mp4,
        )

        ability_videos_v2.additional_properties = d
        return ability_videos_v2

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
