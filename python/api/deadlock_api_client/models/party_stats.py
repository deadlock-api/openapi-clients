from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PartyStats")


@_attrs_define
class PartyStats:
    """
    Attributes:
        matches (list[int]):
        matches_played (int):
        party_size (int):
        wins (int):
    """

    matches: list[int]
    matches_played: int
    party_size: int
    wins: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matches = self.matches

        matches_played = self.matches_played

        party_size = self.party_size

        wins = self.wins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matches": matches,
                "matches_played": matches_played,
                "party_size": party_size,
                "wins": wins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        matches = cast(list[int], d.pop("matches"))

        matches_played = d.pop("matches_played")

        party_size = d.pop("party_size")

        wins = d.pop("wins")

        party_stats = cls(
            matches=matches,
            matches_played=matches_played,
            party_size=party_size,
            wins=wins,
        )

        party_stats.additional_properties = d
        return party_stats

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
