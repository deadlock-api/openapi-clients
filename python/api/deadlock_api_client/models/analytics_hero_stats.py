from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsHeroStats")


@_attrs_define
class AnalyticsHeroStats:
    """
    Attributes:
        hero_id (int): See more: <https://assets.deadlock-api.com/v2/heroes>
        losses (int):
        matches (int):
        matches_per_bucket (int):
        players (int):
        total_assists (int):
        total_boss_damage (int):
        total_creep_damage (int):
        total_deaths (int):
        total_denies (int):
        total_kills (int):
        total_last_hits (int):
        total_max_health (int):
        total_net_worth (int):
        total_neutral_damage (int):
        total_player_damage (int):
        total_player_damage_taken (int):
        total_shots_hit (int):
        total_shots_missed (int):
        wins (int):
        bucket (Union[None, Unset, int]):
    """

    hero_id: int
    losses: int
    matches: int
    matches_per_bucket: int
    players: int
    total_assists: int
    total_boss_damage: int
    total_creep_damage: int
    total_deaths: int
    total_denies: int
    total_kills: int
    total_last_hits: int
    total_max_health: int
    total_net_worth: int
    total_neutral_damage: int
    total_player_damage: int
    total_player_damage_taken: int
    total_shots_hit: int
    total_shots_missed: int
    wins: int
    bucket: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hero_id = self.hero_id

        losses = self.losses

        matches = self.matches

        matches_per_bucket = self.matches_per_bucket

        players = self.players

        total_assists = self.total_assists

        total_boss_damage = self.total_boss_damage

        total_creep_damage = self.total_creep_damage

        total_deaths = self.total_deaths

        total_denies = self.total_denies

        total_kills = self.total_kills

        total_last_hits = self.total_last_hits

        total_max_health = self.total_max_health

        total_net_worth = self.total_net_worth

        total_neutral_damage = self.total_neutral_damage

        total_player_damage = self.total_player_damage

        total_player_damage_taken = self.total_player_damage_taken

        total_shots_hit = self.total_shots_hit

        total_shots_missed = self.total_shots_missed

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
                "hero_id": hero_id,
                "losses": losses,
                "matches": matches,
                "matches_per_bucket": matches_per_bucket,
                "players": players,
                "total_assists": total_assists,
                "total_boss_damage": total_boss_damage,
                "total_creep_damage": total_creep_damage,
                "total_deaths": total_deaths,
                "total_denies": total_denies,
                "total_kills": total_kills,
                "total_last_hits": total_last_hits,
                "total_max_health": total_max_health,
                "total_net_worth": total_net_worth,
                "total_neutral_damage": total_neutral_damage,
                "total_player_damage": total_player_damage,
                "total_player_damage_taken": total_player_damage_taken,
                "total_shots_hit": total_shots_hit,
                "total_shots_missed": total_shots_missed,
                "wins": wins,
            }
        )
        if bucket is not UNSET:
            field_dict["bucket"] = bucket

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hero_id = d.pop("hero_id")

        losses = d.pop("losses")

        matches = d.pop("matches")

        matches_per_bucket = d.pop("matches_per_bucket")

        players = d.pop("players")

        total_assists = d.pop("total_assists")

        total_boss_damage = d.pop("total_boss_damage")

        total_creep_damage = d.pop("total_creep_damage")

        total_deaths = d.pop("total_deaths")

        total_denies = d.pop("total_denies")

        total_kills = d.pop("total_kills")

        total_last_hits = d.pop("total_last_hits")

        total_max_health = d.pop("total_max_health")

        total_net_worth = d.pop("total_net_worth")

        total_neutral_damage = d.pop("total_neutral_damage")

        total_player_damage = d.pop("total_player_damage")

        total_player_damage_taken = d.pop("total_player_damage_taken")

        total_shots_hit = d.pop("total_shots_hit")

        total_shots_missed = d.pop("total_shots_missed")

        wins = d.pop("wins")

        def _parse_bucket(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bucket = _parse_bucket(d.pop("bucket", UNSET))

        analytics_hero_stats = cls(
            hero_id=hero_id,
            losses=losses,
            matches=matches,
            matches_per_bucket=matches_per_bucket,
            players=players,
            total_assists=total_assists,
            total_boss_damage=total_boss_damage,
            total_creep_damage=total_creep_damage,
            total_deaths=total_deaths,
            total_denies=total_denies,
            total_kills=total_kills,
            total_last_hits=total_last_hits,
            total_max_health=total_max_health,
            total_net_worth=total_net_worth,
            total_neutral_damage=total_neutral_damage,
            total_player_damage=total_player_damage,
            total_player_damage_taken=total_player_damage_taken,
            total_shots_hit=total_shots_hit,
            total_shots_missed=total_shots_missed,
            wins=wins,
            bucket=bucket,
        )

        analytics_hero_stats.additional_properties = d
        return analytics_hero_stats

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
