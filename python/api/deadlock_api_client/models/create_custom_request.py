from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCustomRequest")


@_attrs_define
class CreateCustomRequest:
    """
    Attributes:
        callback_url (Union[None, Unset, str]): If a callback url is provided, we will send a POST request to this url
            when the match starts.
        cheats_enabled (Union[None, Unset, bool]):
        duplicate_heroes_enabled (Union[None, Unset, bool]):
        experimental_heroes_enabled (Union[None, Unset, bool]):
        is_publicly_visible (Union[None, Unset, bool]):
        min_roster_size (Union[None, Unset, int]):
        randomize_lanes (Union[None, Unset, bool]):
    """

    callback_url: Union[None, Unset, str] = UNSET
    cheats_enabled: Union[None, Unset, bool] = UNSET
    duplicate_heroes_enabled: Union[None, Unset, bool] = UNSET
    experimental_heroes_enabled: Union[None, Unset, bool] = UNSET
    is_publicly_visible: Union[None, Unset, bool] = UNSET
    min_roster_size: Union[None, Unset, int] = UNSET
    randomize_lanes: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        callback_url: Union[None, Unset, str]
        if isinstance(self.callback_url, Unset):
            callback_url = UNSET
        else:
            callback_url = self.callback_url

        cheats_enabled: Union[None, Unset, bool]
        if isinstance(self.cheats_enabled, Unset):
            cheats_enabled = UNSET
        else:
            cheats_enabled = self.cheats_enabled

        duplicate_heroes_enabled: Union[None, Unset, bool]
        if isinstance(self.duplicate_heroes_enabled, Unset):
            duplicate_heroes_enabled = UNSET
        else:
            duplicate_heroes_enabled = self.duplicate_heroes_enabled

        experimental_heroes_enabled: Union[None, Unset, bool]
        if isinstance(self.experimental_heroes_enabled, Unset):
            experimental_heroes_enabled = UNSET
        else:
            experimental_heroes_enabled = self.experimental_heroes_enabled

        is_publicly_visible: Union[None, Unset, bool]
        if isinstance(self.is_publicly_visible, Unset):
            is_publicly_visible = UNSET
        else:
            is_publicly_visible = self.is_publicly_visible

        min_roster_size: Union[None, Unset, int]
        if isinstance(self.min_roster_size, Unset):
            min_roster_size = UNSET
        else:
            min_roster_size = self.min_roster_size

        randomize_lanes: Union[None, Unset, bool]
        if isinstance(self.randomize_lanes, Unset):
            randomize_lanes = UNSET
        else:
            randomize_lanes = self.randomize_lanes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if callback_url is not UNSET:
            field_dict["callback_url"] = callback_url
        if cheats_enabled is not UNSET:
            field_dict["cheats_enabled"] = cheats_enabled
        if duplicate_heroes_enabled is not UNSET:
            field_dict["duplicate_heroes_enabled"] = duplicate_heroes_enabled
        if experimental_heroes_enabled is not UNSET:
            field_dict["experimental_heroes_enabled"] = experimental_heroes_enabled
        if is_publicly_visible is not UNSET:
            field_dict["is_publicly_visible"] = is_publicly_visible
        if min_roster_size is not UNSET:
            field_dict["min_roster_size"] = min_roster_size
        if randomize_lanes is not UNSET:
            field_dict["randomize_lanes"] = randomize_lanes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_callback_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        callback_url = _parse_callback_url(d.pop("callback_url", UNSET))

        def _parse_cheats_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        cheats_enabled = _parse_cheats_enabled(d.pop("cheats_enabled", UNSET))

        def _parse_duplicate_heroes_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        duplicate_heroes_enabled = _parse_duplicate_heroes_enabled(d.pop("duplicate_heroes_enabled", UNSET))

        def _parse_experimental_heroes_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        experimental_heroes_enabled = _parse_experimental_heroes_enabled(d.pop("experimental_heroes_enabled", UNSET))

        def _parse_is_publicly_visible(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_publicly_visible = _parse_is_publicly_visible(d.pop("is_publicly_visible", UNSET))

        def _parse_min_roster_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        min_roster_size = _parse_min_roster_size(d.pop("min_roster_size", UNSET))

        def _parse_randomize_lanes(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        randomize_lanes = _parse_randomize_lanes(d.pop("randomize_lanes", UNSET))

        create_custom_request = cls(
            callback_url=callback_url,
            cheats_enabled=cheats_enabled,
            duplicate_heroes_enabled=duplicate_heroes_enabled,
            experimental_heroes_enabled=experimental_heroes_enabled,
            is_publicly_visible=is_publicly_visible,
            min_roster_size=min_roster_size,
            randomize_lanes=randomize_lanes,
        )

        create_custom_request.additional_properties = d
        return create_custom_request

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
