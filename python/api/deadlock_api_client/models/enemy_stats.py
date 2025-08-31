from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EnemyStats")


@_attrs_define
class EnemyStats:
    """
    Attributes:
        enemy_id (int):
        matches (list[int]):
        matches_played (int):
        wins (int): The amount of matches won against the enemy.
    """

    enemy_id: int
    matches: list[int]
    matches_played: int
    wins: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enemy_id = self.enemy_id

        matches = self.matches

        matches_played = self.matches_played

        wins = self.wins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enemy_id": enemy_id,
                "matches": matches,
                "matches_played": matches_played,
                "wins": wins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enemy_id = d.pop("enemy_id")

        matches = cast(list[int], d.pop("matches"))

        matches_played = d.pop("matches_played")

        wins = d.pop("wins")

        enemy_stats = cls(
            enemy_id=enemy_id,
            matches=matches,
            matches_played=matches_played,
            wins=wins,
        )

        enemy_stats.additional_properties = d
        return enemy_stats

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
