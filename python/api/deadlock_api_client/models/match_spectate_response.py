from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchSpectateResponse")


@_attrs_define
class MatchSpectateResponse:
    """
    Attributes:
        broadcast_url (str):
        lobby_id (Union[None, Unset, int]):
    """

    broadcast_url: str
    lobby_id: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        broadcast_url = self.broadcast_url

        lobby_id: Union[None, Unset, int]
        if isinstance(self.lobby_id, Unset):
            lobby_id = UNSET
        else:
            lobby_id = self.lobby_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "broadcast_url": broadcast_url,
            }
        )
        if lobby_id is not UNSET:
            field_dict["lobby_id"] = lobby_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        broadcast_url = d.pop("broadcast_url")

        def _parse_lobby_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        lobby_id = _parse_lobby_id(d.pop("lobby_id", UNSET))

        match_spectate_response = cls(
            broadcast_url=broadcast_url,
            lobby_id=lobby_id,
        )

        match_spectate_response.additional_properties = d
        return match_spectate_response

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
