from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerCardSlotHero")


@_attrs_define
class PlayerCardSlotHero:
    """
    Attributes:
        id (Union[None, Unset, int]): See more: <https://assets.deadlock-api.com/v2/heroes>
        kills (Union[None, Unset, int]):
        wins (Union[None, Unset, int]):
    """

    id: Union[None, Unset, int] = UNSET
    kills: Union[None, Unset, int] = UNSET
    wins: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        kills: Union[None, Unset, int]
        if isinstance(self.kills, Unset):
            kills = UNSET
        else:
            kills = self.kills

        wins: Union[None, Unset, int]
        if isinstance(self.wins, Unset):
            wins = UNSET
        else:
            wins = self.wins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if kills is not UNSET:
            field_dict["kills"] = kills
        if wins is not UNSET:
            field_dict["wins"] = wins

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_kills(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        kills = _parse_kills(d.pop("kills", UNSET))

        def _parse_wins(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wins = _parse_wins(d.pop("wins", UNSET))

        player_card_slot_hero = cls(
            id=id,
            kills=kills,
            wins=wins,
        )

        player_card_slot_hero.additional_properties = d
        return player_card_slot_hero

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
