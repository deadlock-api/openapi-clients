from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HeroCombStats")


@_attrs_define
class HeroCombStats:
    """
    Attributes:
        hero_ids (list[int]): See more: <https://assets.deadlock-api.com/v2/heroes>
        losses (int):
        matches (int):
        wins (int):
    """

    hero_ids: list[int]
    losses: int
    matches: int
    wins: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hero_ids = self.hero_ids

        losses = self.losses

        matches = self.matches

        wins = self.wins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hero_ids": hero_ids,
                "losses": losses,
                "matches": matches,
                "wins": wins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hero_ids = cast(list[int], d.pop("hero_ids"))

        losses = d.pop("losses")

        matches = d.pop("matches")

        wins = d.pop("wins")

        hero_comb_stats = cls(
            hero_ids=hero_ids,
            losses=losses,
            matches=matches,
            wins=wins,
        )

        hero_comb_stats.additional_properties = d
        return hero_comb_stats

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
