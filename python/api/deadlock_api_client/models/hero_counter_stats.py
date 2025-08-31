from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HeroCounterStats")


@_attrs_define
class HeroCounterStats:
    """
    Attributes:
        assists (int): The number of assists by `hero_id` when facing `enemy_hero_id`.
        creeps (int): The number of creeps killed by `hero_id` when facing `enemy_hero_id`.
        deaths (int): The number of deaths by `hero_id` when facing `enemy_hero_id`.
        denies (int): The number of denies by `hero_id` when facing `enemy_hero_id`.
        enemy_assists (int): The number of assists by `enemy_hero_id` when facing `hero_id`.
        enemy_creeps (int): The number of creeps killed by `enemy_hero_id` when facing `hero_id`.
        enemy_deaths (int): The number of deaths by `enemy_hero_id` when facing `hero_id`.
        enemy_denies (int): The number of denies by `enemy_hero_id` when facing `hero_id`.
        enemy_hero_id (int): The ID of the opposing hero. See more: <https://assets.deadlock-api.com/v2/heroes>
        enemy_kills (int): The number of kills by `enemy_hero_id` when facing `hero_id`.
        enemy_last_hits (int): The number of last hits by `enemy_hero_id` when facing `hero_id`.
        enemy_networth (int): The net worth of `enemy_hero_id` when facing `hero_id`.
        enemy_obj_damage (int): The amount of objective damage dealt by `enemy_hero_id` when facing `hero_id`.
        hero_id (int): The ID of the hero. See more: <https://assets.deadlock-api.com/v2/heroes>
        kills (int): The number of kills by `hero_id` when facing `enemy_hero_id`.
        last_hits (int): The number of last hits by `hero_id` when facing `enemy_hero_id`.
        matches_played (int): The total number of matches played between `hero_id` and `enemy_hero_id` that meet the
            filter criteria.
        networth (int): The net worth of `hero_id` when facing `enemy_hero_id`.
        obj_damage (int): The amount of objective damage dealt by `hero_id` when facing `enemy_hero_id`.
        wins (int): The number of times `hero_id` won the match when facing `enemy_hero_id`.
    """

    assists: int
    creeps: int
    deaths: int
    denies: int
    enemy_assists: int
    enemy_creeps: int
    enemy_deaths: int
    enemy_denies: int
    enemy_hero_id: int
    enemy_kills: int
    enemy_last_hits: int
    enemy_networth: int
    enemy_obj_damage: int
    hero_id: int
    kills: int
    last_hits: int
    matches_played: int
    networth: int
    obj_damage: int
    wins: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assists = self.assists

        creeps = self.creeps

        deaths = self.deaths

        denies = self.denies

        enemy_assists = self.enemy_assists

        enemy_creeps = self.enemy_creeps

        enemy_deaths = self.enemy_deaths

        enemy_denies = self.enemy_denies

        enemy_hero_id = self.enemy_hero_id

        enemy_kills = self.enemy_kills

        enemy_last_hits = self.enemy_last_hits

        enemy_networth = self.enemy_networth

        enemy_obj_damage = self.enemy_obj_damage

        hero_id = self.hero_id

        kills = self.kills

        last_hits = self.last_hits

        matches_played = self.matches_played

        networth = self.networth

        obj_damage = self.obj_damage

        wins = self.wins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assists": assists,
                "creeps": creeps,
                "deaths": deaths,
                "denies": denies,
                "enemy_assists": enemy_assists,
                "enemy_creeps": enemy_creeps,
                "enemy_deaths": enemy_deaths,
                "enemy_denies": enemy_denies,
                "enemy_hero_id": enemy_hero_id,
                "enemy_kills": enemy_kills,
                "enemy_last_hits": enemy_last_hits,
                "enemy_networth": enemy_networth,
                "enemy_obj_damage": enemy_obj_damage,
                "hero_id": hero_id,
                "kills": kills,
                "last_hits": last_hits,
                "matches_played": matches_played,
                "networth": networth,
                "obj_damage": obj_damage,
                "wins": wins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assists = d.pop("assists")

        creeps = d.pop("creeps")

        deaths = d.pop("deaths")

        denies = d.pop("denies")

        enemy_assists = d.pop("enemy_assists")

        enemy_creeps = d.pop("enemy_creeps")

        enemy_deaths = d.pop("enemy_deaths")

        enemy_denies = d.pop("enemy_denies")

        enemy_hero_id = d.pop("enemy_hero_id")

        enemy_kills = d.pop("enemy_kills")

        enemy_last_hits = d.pop("enemy_last_hits")

        enemy_networth = d.pop("enemy_networth")

        enemy_obj_damage = d.pop("enemy_obj_damage")

        hero_id = d.pop("hero_id")

        kills = d.pop("kills")

        last_hits = d.pop("last_hits")

        matches_played = d.pop("matches_played")

        networth = d.pop("networth")

        obj_damage = d.pop("obj_damage")

        wins = d.pop("wins")

        hero_counter_stats = cls(
            assists=assists,
            creeps=creeps,
            deaths=deaths,
            denies=denies,
            enemy_assists=enemy_assists,
            enemy_creeps=enemy_creeps,
            enemy_deaths=enemy_deaths,
            enemy_denies=enemy_denies,
            enemy_hero_id=enemy_hero_id,
            enemy_kills=enemy_kills,
            enemy_last_hits=enemy_last_hits,
            enemy_networth=enemy_networth,
            enemy_obj_damage=enemy_obj_damage,
            hero_id=hero_id,
            kills=kills,
            last_hits=last_hits,
            matches_played=matches_played,
            networth=networth,
            obj_damage=obj_damage,
            wins=wins,
        )

        hero_counter_stats.additional_properties = d
        return hero_counter_stats

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
