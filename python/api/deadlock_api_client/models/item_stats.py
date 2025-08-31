from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemStats")


@_attrs_define
class ItemStats:
    """
    Attributes:
        item_id (int): See more: <https://assets.deadlock-api.com/v2/items>
        losses (int):
        matches (int):
        players (int):
        wins (int):
        bucket (Union[None, Unset, int]):
    """

    item_id: int
    losses: int
    matches: int
    players: int
    wins: int
    bucket: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        losses = self.losses

        matches = self.matches

        players = self.players

        wins = self.wins

        bucket: Union[None, Unset, int]
        if isinstance(self.bucket, Unset):
            bucket = UNSET
        else:
            bucket = self.bucket

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
                "losses": losses,
                "matches": matches,
                "players": players,
                "wins": wins,
            }
        )
        if bucket is not UNSET:
            field_dict["bucket"] = bucket

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = d.pop("item_id")

        losses = d.pop("losses")

        matches = d.pop("matches")

        players = d.pop("players")

        wins = d.pop("wins")

        def _parse_bucket(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bucket = _parse_bucket(d.pop("bucket", UNSET))

        item_stats = cls(
            item_id=item_id,
            losses=losses,
            matches=matches,
            players=players,
            wins=wins,
            bucket=bucket,
        )

        item_stats.additional_properties = d
        return item_stats

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
