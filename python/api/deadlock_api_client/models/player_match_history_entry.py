from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerMatchHistoryEntry")


@_attrs_define
class PlayerMatchHistoryEntry:
    """
    Attributes:
        account_id (int):
        denies (int):
        game_mode (int):
        hero_id (int): See more: <https://assets.deadlock-api.com/v2/heroes>
        hero_level (int):
        last_hits (int):
        match_duration_s (int):
        match_id (int):
        match_mode (int):
        match_result (int):
        net_worth (int):
        objectives_mask_team0 (int):
        objectives_mask_team1 (int):
        player_assists (int):
        player_deaths (int):
        player_kills (int):
        player_team (int):
        start_time (int):
        abandoned_time_s (Union[None, Unset, int]):
        team_abandoned (Union[None, Unset, bool]):
    """

    account_id: int
    denies: int
    game_mode: int
    hero_id: int
    hero_level: int
    last_hits: int
    match_duration_s: int
    match_id: int
    match_mode: int
    match_result: int
    net_worth: int
    objectives_mask_team0: int
    objectives_mask_team1: int
    player_assists: int
    player_deaths: int
    player_kills: int
    player_team: int
    start_time: int
    abandoned_time_s: Union[None, Unset, int] = UNSET
    team_abandoned: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        denies = self.denies

        game_mode = self.game_mode

        hero_id = self.hero_id

        hero_level = self.hero_level

        last_hits = self.last_hits

        match_duration_s = self.match_duration_s

        match_id = self.match_id

        match_mode = self.match_mode

        match_result = self.match_result

        net_worth = self.net_worth

        objectives_mask_team0 = self.objectives_mask_team0

        objectives_mask_team1 = self.objectives_mask_team1

        player_assists = self.player_assists

        player_deaths = self.player_deaths

        player_kills = self.player_kills

        player_team = self.player_team

        start_time = self.start_time

        abandoned_time_s: Union[None, Unset, int]
        if isinstance(self.abandoned_time_s, Unset):
            abandoned_time_s = UNSET
        else:
            abandoned_time_s = self.abandoned_time_s

        team_abandoned: Union[None, Unset, bool]
        if isinstance(self.team_abandoned, Unset):
            team_abandoned = UNSET
        else:
            team_abandoned = self.team_abandoned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "denies": denies,
                "game_mode": game_mode,
                "hero_id": hero_id,
                "hero_level": hero_level,
                "last_hits": last_hits,
                "match_duration_s": match_duration_s,
                "match_id": match_id,
                "match_mode": match_mode,
                "match_result": match_result,
                "net_worth": net_worth,
                "objectives_mask_team0": objectives_mask_team0,
                "objectives_mask_team1": objectives_mask_team1,
                "player_assists": player_assists,
                "player_deaths": player_deaths,
                "player_kills": player_kills,
                "player_team": player_team,
                "start_time": start_time,
            }
        )
        if abandoned_time_s is not UNSET:
            field_dict["abandoned_time_s"] = abandoned_time_s
        if team_abandoned is not UNSET:
            field_dict["team_abandoned"] = team_abandoned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        denies = d.pop("denies")

        game_mode = d.pop("game_mode")

        hero_id = d.pop("hero_id")

        hero_level = d.pop("hero_level")

        last_hits = d.pop("last_hits")

        match_duration_s = d.pop("match_duration_s")

        match_id = d.pop("match_id")

        match_mode = d.pop("match_mode")

        match_result = d.pop("match_result")

        net_worth = d.pop("net_worth")

        objectives_mask_team0 = d.pop("objectives_mask_team0")

        objectives_mask_team1 = d.pop("objectives_mask_team1")

        player_assists = d.pop("player_assists")

        player_deaths = d.pop("player_deaths")

        player_kills = d.pop("player_kills")

        player_team = d.pop("player_team")

        start_time = d.pop("start_time")

        def _parse_abandoned_time_s(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        abandoned_time_s = _parse_abandoned_time_s(d.pop("abandoned_time_s", UNSET))

        def _parse_team_abandoned(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        team_abandoned = _parse_team_abandoned(d.pop("team_abandoned", UNSET))

        player_match_history_entry = cls(
            account_id=account_id,
            denies=denies,
            game_mode=game_mode,
            hero_id=hero_id,
            hero_level=hero_level,
            last_hits=last_hits,
            match_duration_s=match_duration_s,
            match_id=match_id,
            match_mode=match_mode,
            match_result=match_result,
            net_worth=net_worth,
            objectives_mask_team0=objectives_mask_team0,
            objectives_mask_team1=objectives_mask_team1,
            player_assists=player_assists,
            player_deaths=player_deaths,
            player_kills=player_kills,
            player_team=player_team,
            start_time=start_time,
            abandoned_time_s=abandoned_time_s,
            team_abandoned=team_abandoned,
        )

        player_match_history_entry.additional_properties = d
        return player_match_history_entry

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
