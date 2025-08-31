from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MateStats")


@_attrs_define
class MateStats:
    """
    Attributes:
        matches (list[int]):
        matches_played (int):
        mate_id (int):
        wins (int):
    """

    matches: list[int]
    matches_played: int
    mate_id: int
    wins: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matches = self.matches

        matches_played = self.matches_played

        mate_id = self.mate_id

        wins = self.wins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matches": matches,
                "matches_played": matches_played,
                "mate_id": mate_id,
                "wins": wins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        matches = cast(list[int], d.pop("matches"))

        matches_played = d.pop("matches_played")

        mate_id = d.pop("mate_id")

        wins = d.pop("wins")

        mate_stats = cls(
            matches=matches,
            matches_played=matches_played,
            mate_id=mate_id,
            wins=wins,
        )

        mate_stats.additional_properties = d
        return mate_stats

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
