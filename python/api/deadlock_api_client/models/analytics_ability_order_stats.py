from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsAbilityOrderStats")


@_attrs_define
class AnalyticsAbilityOrderStats:
    """
    Attributes:
        abilities (list[int]): See more: <https://assets.deadlock-api.com/v2/heroes>
        losses (int):
        matches (int):
        players (int):
        total_assists (int):
        total_deaths (int):
        total_kills (int):
        wins (int):
    """

    abilities: list[int]
    losses: int
    matches: int
    players: int
    total_assists: int
    total_deaths: int
    total_kills: int
    wins: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abilities = self.abilities

        losses = self.losses

        matches = self.matches

        players = self.players

        total_assists = self.total_assists

        total_deaths = self.total_deaths

        total_kills = self.total_kills

        wins = self.wins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "abilities": abilities,
                "losses": losses,
                "matches": matches,
                "players": players,
                "total_assists": total_assists,
                "total_deaths": total_deaths,
                "total_kills": total_kills,
                "wins": wins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        abilities = cast(list[int], d.pop("abilities"))

        losses = d.pop("losses")

        matches = d.pop("matches")

        players = d.pop("players")

        total_assists = d.pop("total_assists")

        total_deaths = d.pop("total_deaths")

        total_kills = d.pop("total_kills")

        wins = d.pop("wins")

        analytics_ability_order_stats = cls(
            abilities=abilities,
            losses=losses,
            matches=matches,
            players=players,
            total_assists=total_assists,
            total_deaths=total_deaths,
            total_kills=total_kills,
            wins=wins,
        )

        analytics_ability_order_stats.additional_properties = d
        return analytics_ability_order_stats

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
