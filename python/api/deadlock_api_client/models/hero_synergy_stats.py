from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HeroSynergyStats")


@_attrs_define
class HeroSynergyStats:
    """
    Attributes:
        assists1 (int): The number of assists by `hero_id1` when playing with `hero_id2`.
        assists2 (int): The number of assists by `hero_id2` when playing with `hero_id1`.
        creeps1 (int): The number of creeps killed by `hero_id1` when playing with `hero_id2`.
        creeps2 (int): The number of creeps killed by `hero_id2` when playing with `hero_id1`.
        deaths1 (int): The number of deaths by `hero_id1` when playing with `hero_id2`.
        deaths2 (int): The number of deaths by `hero_id2` when playing with `hero_id1`.
        denies1 (int): The number of denies by `hero_id1` when playing with `hero_id2`.
        denies2 (int): The number of denies by `hero_id2` when playing with `hero_id1`.
        hero_id1 (int): The ID of the first hero in the pair.
        hero_id2 (int): The ID of the second hero in the pair.
        kills1 (int): The number of kills by `hero_id1` when playing with `hero_id2`.
        kills2 (int): The number of kills by `hero_id2` when playing with `hero_id1`.
        last_hits1 (int): The number of last hits by `hero_id1` when playing with `hero_id2`.
        last_hits2 (int): The number of last hits by `hero_id2` when playing with `hero_id1`.
        matches_played (int): The total number of matches played where `hero_id1` and `hero_id2` were on the same team,
            meeting the filter criteria.
        networth1 (int): The net worth of `hero_id1` when playing with `hero_id2`.
        networth2 (int): The net worth of `hero_id2` when playing with `hero_id1`.
        obj_damage1 (int): The amount of objective damage dealt by `hero_id1` when playing with `hero_id2`.
        obj_damage2 (int): The amount of objective damage dealt by `hero_id2` when playing with `hero_id1`.
        wins (int): The number of times the team won when both `hero_id1` and `hero_id2` were on the same team.
    """

    assists1: int
    assists2: int
    creeps1: int
    creeps2: int
    deaths1: int
    deaths2: int
    denies1: int
    denies2: int
    hero_id1: int
    hero_id2: int
    kills1: int
    kills2: int
    last_hits1: int
    last_hits2: int
    matches_played: int
    networth1: int
    networth2: int
    obj_damage1: int
    obj_damage2: int
    wins: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assists1 = self.assists1

        assists2 = self.assists2

        creeps1 = self.creeps1

        creeps2 = self.creeps2

        deaths1 = self.deaths1

        deaths2 = self.deaths2

        denies1 = self.denies1

        denies2 = self.denies2

        hero_id1 = self.hero_id1

        hero_id2 = self.hero_id2

        kills1 = self.kills1

        kills2 = self.kills2

        last_hits1 = self.last_hits1

        last_hits2 = self.last_hits2

        matches_played = self.matches_played

        networth1 = self.networth1

        networth2 = self.networth2

        obj_damage1 = self.obj_damage1

        obj_damage2 = self.obj_damage2

        wins = self.wins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assists1": assists1,
                "assists2": assists2,
                "creeps1": creeps1,
                "creeps2": creeps2,
                "deaths1": deaths1,
                "deaths2": deaths2,
                "denies1": denies1,
                "denies2": denies2,
                "hero_id1": hero_id1,
                "hero_id2": hero_id2,
                "kills1": kills1,
                "kills2": kills2,
                "last_hits1": last_hits1,
                "last_hits2": last_hits2,
                "matches_played": matches_played,
                "networth1": networth1,
                "networth2": networth2,
                "obj_damage1": obj_damage1,
                "obj_damage2": obj_damage2,
                "wins": wins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assists1 = d.pop("assists1")

        assists2 = d.pop("assists2")

        creeps1 = d.pop("creeps1")

        creeps2 = d.pop("creeps2")

        deaths1 = d.pop("deaths1")

        deaths2 = d.pop("deaths2")

        denies1 = d.pop("denies1")

        denies2 = d.pop("denies2")

        hero_id1 = d.pop("hero_id1")

        hero_id2 = d.pop("hero_id2")

        kills1 = d.pop("kills1")

        kills2 = d.pop("kills2")

        last_hits1 = d.pop("last_hits1")

        last_hits2 = d.pop("last_hits2")

        matches_played = d.pop("matches_played")

        networth1 = d.pop("networth1")

        networth2 = d.pop("networth2")

        obj_damage1 = d.pop("obj_damage1")

        obj_damage2 = d.pop("obj_damage2")

        wins = d.pop("wins")

        hero_synergy_stats = cls(
            assists1=assists1,
            assists2=assists2,
            creeps1=creeps1,
            creeps2=creeps2,
            deaths1=deaths1,
            deaths2=deaths2,
            denies1=denies1,
            denies2=denies2,
            hero_id1=hero_id1,
            hero_id2=hero_id2,
            kills1=kills1,
            kills2=kills2,
            last_hits1=last_hits1,
            last_hits2=last_hits2,
            matches_played=matches_played,
            networth1=networth1,
            networth2=networth2,
            obj_damage1=obj_damage1,
            obj_damage2=obj_damage2,
            wins=wins,
        )

        hero_synergy_stats.additional_properties = d
        return hero_synergy_stats

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
