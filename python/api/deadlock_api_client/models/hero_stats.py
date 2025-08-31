from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HeroStats")


@_attrs_define
class HeroStats:
    """
    Attributes:
        account_id (int):
        accuracy (float):
        assists (int):
        assists_per_min (float):
        creeps_per_min (float):
        crit_shot_rate (float):
        damage_mitigated_per_min (float):
        damage_per_min (float):
        damage_per_soul (float):
        damage_taken_per_min (float):
        damage_taken_per_soul (float):
        deaths (int):
        deaths_per_min (float):
        denies_per_match (float):
        denies_per_min (float):
        ending_level (float):
        hero_id (int): See more: <https://assets.deadlock-api.com/v2/heroes>
        kills (int):
        kills_per_min (float):
        last_hits_per_min (float):
        last_played (int):
        matches (list[int]):
        matches_played (int):
        networth_per_min (float):
        obj_damage_per_min (float):
        obj_damage_per_soul (float):
        time_played (int):
        wins (int):
    """

    account_id: int
    accuracy: float
    assists: int
    assists_per_min: float
    creeps_per_min: float
    crit_shot_rate: float
    damage_mitigated_per_min: float
    damage_per_min: float
    damage_per_soul: float
    damage_taken_per_min: float
    damage_taken_per_soul: float
    deaths: int
    deaths_per_min: float
    denies_per_match: float
    denies_per_min: float
    ending_level: float
    hero_id: int
    kills: int
    kills_per_min: float
    last_hits_per_min: float
    last_played: int
    matches: list[int]
    matches_played: int
    networth_per_min: float
    obj_damage_per_min: float
    obj_damage_per_soul: float
    time_played: int
    wins: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        accuracy = self.accuracy

        assists = self.assists

        assists_per_min = self.assists_per_min

        creeps_per_min = self.creeps_per_min

        crit_shot_rate = self.crit_shot_rate

        damage_mitigated_per_min = self.damage_mitigated_per_min

        damage_per_min = self.damage_per_min

        damage_per_soul = self.damage_per_soul

        damage_taken_per_min = self.damage_taken_per_min

        damage_taken_per_soul = self.damage_taken_per_soul

        deaths = self.deaths

        deaths_per_min = self.deaths_per_min

        denies_per_match = self.denies_per_match

        denies_per_min = self.denies_per_min

        ending_level = self.ending_level

        hero_id = self.hero_id

        kills = self.kills

        kills_per_min = self.kills_per_min

        last_hits_per_min = self.last_hits_per_min

        last_played = self.last_played

        matches = self.matches

        matches_played = self.matches_played

        networth_per_min = self.networth_per_min

        obj_damage_per_min = self.obj_damage_per_min

        obj_damage_per_soul = self.obj_damage_per_soul

        time_played = self.time_played

        wins = self.wins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "accuracy": accuracy,
                "assists": assists,
                "assists_per_min": assists_per_min,
                "creeps_per_min": creeps_per_min,
                "crit_shot_rate": crit_shot_rate,
                "damage_mitigated_per_min": damage_mitigated_per_min,
                "damage_per_min": damage_per_min,
                "damage_per_soul": damage_per_soul,
                "damage_taken_per_min": damage_taken_per_min,
                "damage_taken_per_soul": damage_taken_per_soul,
                "deaths": deaths,
                "deaths_per_min": deaths_per_min,
                "denies_per_match": denies_per_match,
                "denies_per_min": denies_per_min,
                "ending_level": ending_level,
                "hero_id": hero_id,
                "kills": kills,
                "kills_per_min": kills_per_min,
                "last_hits_per_min": last_hits_per_min,
                "last_played": last_played,
                "matches": matches,
                "matches_played": matches_played,
                "networth_per_min": networth_per_min,
                "obj_damage_per_min": obj_damage_per_min,
                "obj_damage_per_soul": obj_damage_per_soul,
                "time_played": time_played,
                "wins": wins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        accuracy = d.pop("accuracy")

        assists = d.pop("assists")

        assists_per_min = d.pop("assists_per_min")

        creeps_per_min = d.pop("creeps_per_min")

        crit_shot_rate = d.pop("crit_shot_rate")

        damage_mitigated_per_min = d.pop("damage_mitigated_per_min")

        damage_per_min = d.pop("damage_per_min")

        damage_per_soul = d.pop("damage_per_soul")

        damage_taken_per_min = d.pop("damage_taken_per_min")

        damage_taken_per_soul = d.pop("damage_taken_per_soul")

        deaths = d.pop("deaths")

        deaths_per_min = d.pop("deaths_per_min")

        denies_per_match = d.pop("denies_per_match")

        denies_per_min = d.pop("denies_per_min")

        ending_level = d.pop("ending_level")

        hero_id = d.pop("hero_id")

        kills = d.pop("kills")

        kills_per_min = d.pop("kills_per_min")

        last_hits_per_min = d.pop("last_hits_per_min")

        last_played = d.pop("last_played")

        matches = cast(list[int], d.pop("matches"))

        matches_played = d.pop("matches_played")

        networth_per_min = d.pop("networth_per_min")

        obj_damage_per_min = d.pop("obj_damage_per_min")

        obj_damage_per_soul = d.pop("obj_damage_per_soul")

        time_played = d.pop("time_played")

        wins = d.pop("wins")

        hero_stats = cls(
            account_id=account_id,
            accuracy=accuracy,
            assists=assists,
            assists_per_min=assists_per_min,
            creeps_per_min=creeps_per_min,
            crit_shot_rate=crit_shot_rate,
            damage_mitigated_per_min=damage_mitigated_per_min,
            damage_per_min=damage_per_min,
            damage_per_soul=damage_per_soul,
            damage_taken_per_min=damage_taken_per_min,
            damage_taken_per_soul=damage_taken_per_soul,
            deaths=deaths,
            deaths_per_min=deaths_per_min,
            denies_per_match=denies_per_match,
            denies_per_min=denies_per_min,
            ending_level=ending_level,
            hero_id=hero_id,
            kills=kills,
            kills_per_min=kills_per_min,
            last_hits_per_min=last_hits_per_min,
            last_played=last_played,
            matches=matches,
            matches_played=matches_played,
            networth_per_min=networth_per_min,
            obj_damage_per_min=obj_damage_per_min,
            obj_damage_per_soul=obj_damage_per_soul,
            time_played=time_played,
            wins=wins,
        )

        hero_stats.additional_properties = d
        return hero_stats

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
