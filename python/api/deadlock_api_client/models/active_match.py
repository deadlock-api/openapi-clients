from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.active_match_game_mode import ActiveMatchGameMode
from ..models.active_match_mode import ActiveMatchMode
from ..models.active_match_region_mode import ActiveMatchRegionMode
from ..models.active_match_team import ActiveMatchTeam
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.active_match_player import ActiveMatchPlayer


T = TypeVar("T", bound="ActiveMatch")


@_attrs_define
class ActiveMatch:
    """
    Attributes:
        players (list['ActiveMatchPlayer']):
        compat_version (Union[None, Unset, int]):
        duration_s (Union[None, Unset, int]):
        game_mode (Union[None, Unset, int]):
        game_mode_parsed (Union[ActiveMatchGameMode, None, Unset]):
        game_mode_version (Union[None, Unset, int]):
        lobby_id (Union[None, Unset, int]):
        match_id (Union[None, Unset, int]):
        match_mode (Union[None, Unset, int]):
        match_mode_parsed (Union[ActiveMatchMode, None, Unset]):
        match_score (Union[None, Unset, int]):
        net_worth_team_0 (Union[None, Unset, int]):
        net_worth_team_1 (Union[None, Unset, int]):
        objectives_mask_team0 (Union[None, Unset, int]):
        objectives_mask_team1 (Union[None, Unset, int]):
        open_spectator_slots (Union[None, Unset, int]):
        region_mode (Union[None, Unset, int]):
        region_mode_parsed (Union[ActiveMatchRegionMode, None, Unset]):
        spectators (Union[None, Unset, int]):
        start_time (Union[None, Unset, int]):
        winning_team (Union[None, Unset, int]):
        winning_team_parsed (Union[ActiveMatchTeam, None, Unset]):
    """

    players: list["ActiveMatchPlayer"]
    compat_version: Union[None, Unset, int] = UNSET
    duration_s: Union[None, Unset, int] = UNSET
    game_mode: Union[None, Unset, int] = UNSET
    game_mode_parsed: Union[ActiveMatchGameMode, None, Unset] = UNSET
    game_mode_version: Union[None, Unset, int] = UNSET
    lobby_id: Union[None, Unset, int] = UNSET
    match_id: Union[None, Unset, int] = UNSET
    match_mode: Union[None, Unset, int] = UNSET
    match_mode_parsed: Union[ActiveMatchMode, None, Unset] = UNSET
    match_score: Union[None, Unset, int] = UNSET
    net_worth_team_0: Union[None, Unset, int] = UNSET
    net_worth_team_1: Union[None, Unset, int] = UNSET
    objectives_mask_team0: Union[None, Unset, int] = UNSET
    objectives_mask_team1: Union[None, Unset, int] = UNSET
    open_spectator_slots: Union[None, Unset, int] = UNSET
    region_mode: Union[None, Unset, int] = UNSET
    region_mode_parsed: Union[ActiveMatchRegionMode, None, Unset] = UNSET
    spectators: Union[None, Unset, int] = UNSET
    start_time: Union[None, Unset, int] = UNSET
    winning_team: Union[None, Unset, int] = UNSET
    winning_team_parsed: Union[ActiveMatchTeam, None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)

        compat_version: Union[None, Unset, int]
        if isinstance(self.compat_version, Unset):
            compat_version = UNSET
        else:
            compat_version = self.compat_version

        duration_s: Union[None, Unset, int]
        if isinstance(self.duration_s, Unset):
            duration_s = UNSET
        else:
            duration_s = self.duration_s

        game_mode: Union[None, Unset, int]
        if isinstance(self.game_mode, Unset):
            game_mode = UNSET
        else:
            game_mode = self.game_mode

        game_mode_parsed: Union[None, Unset, str]
        if isinstance(self.game_mode_parsed, Unset):
            game_mode_parsed = UNSET
        elif isinstance(self.game_mode_parsed, ActiveMatchGameMode):
            game_mode_parsed = self.game_mode_parsed.value
        else:
            game_mode_parsed = self.game_mode_parsed

        game_mode_version: Union[None, Unset, int]
        if isinstance(self.game_mode_version, Unset):
            game_mode_version = UNSET
        else:
            game_mode_version = self.game_mode_version

        lobby_id: Union[None, Unset, int]
        if isinstance(self.lobby_id, Unset):
            lobby_id = UNSET
        else:
            lobby_id = self.lobby_id

        match_id: Union[None, Unset, int]
        if isinstance(self.match_id, Unset):
            match_id = UNSET
        else:
            match_id = self.match_id

        match_mode: Union[None, Unset, int]
        if isinstance(self.match_mode, Unset):
            match_mode = UNSET
        else:
            match_mode = self.match_mode

        match_mode_parsed: Union[None, Unset, str]
        if isinstance(self.match_mode_parsed, Unset):
            match_mode_parsed = UNSET
        elif isinstance(self.match_mode_parsed, ActiveMatchMode):
            match_mode_parsed = self.match_mode_parsed.value
        else:
            match_mode_parsed = self.match_mode_parsed

        match_score: Union[None, Unset, int]
        if isinstance(self.match_score, Unset):
            match_score = UNSET
        else:
            match_score = self.match_score

        net_worth_team_0: Union[None, Unset, int]
        if isinstance(self.net_worth_team_0, Unset):
            net_worth_team_0 = UNSET
        else:
            net_worth_team_0 = self.net_worth_team_0

        net_worth_team_1: Union[None, Unset, int]
        if isinstance(self.net_worth_team_1, Unset):
            net_worth_team_1 = UNSET
        else:
            net_worth_team_1 = self.net_worth_team_1

        objectives_mask_team0: Union[None, Unset, int]
        if isinstance(self.objectives_mask_team0, Unset):
            objectives_mask_team0 = UNSET
        else:
            objectives_mask_team0 = self.objectives_mask_team0

        objectives_mask_team1: Union[None, Unset, int]
        if isinstance(self.objectives_mask_team1, Unset):
            objectives_mask_team1 = UNSET
        else:
            objectives_mask_team1 = self.objectives_mask_team1

        open_spectator_slots: Union[None, Unset, int]
        if isinstance(self.open_spectator_slots, Unset):
            open_spectator_slots = UNSET
        else:
            open_spectator_slots = self.open_spectator_slots

        region_mode: Union[None, Unset, int]
        if isinstance(self.region_mode, Unset):
            region_mode = UNSET
        else:
            region_mode = self.region_mode

        region_mode_parsed: Union[None, Unset, str]
        if isinstance(self.region_mode_parsed, Unset):
            region_mode_parsed = UNSET
        elif isinstance(self.region_mode_parsed, ActiveMatchRegionMode):
            region_mode_parsed = self.region_mode_parsed.value
        else:
            region_mode_parsed = self.region_mode_parsed

        spectators: Union[None, Unset, int]
        if isinstance(self.spectators, Unset):
            spectators = UNSET
        else:
            spectators = self.spectators

        start_time: Union[None, Unset, int]
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        else:
            start_time = self.start_time

        winning_team: Union[None, Unset, int]
        if isinstance(self.winning_team, Unset):
            winning_team = UNSET
        else:
            winning_team = self.winning_team

        winning_team_parsed: Union[None, Unset, str]
        if isinstance(self.winning_team_parsed, Unset):
            winning_team_parsed = UNSET
        elif isinstance(self.winning_team_parsed, ActiveMatchTeam):
            winning_team_parsed = self.winning_team_parsed.value
        else:
            winning_team_parsed = self.winning_team_parsed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "players": players,
            }
        )
        if compat_version is not UNSET:
            field_dict["compat_version"] = compat_version
        if duration_s is not UNSET:
            field_dict["duration_s"] = duration_s
        if game_mode is not UNSET:
            field_dict["game_mode"] = game_mode
        if game_mode_parsed is not UNSET:
            field_dict["game_mode_parsed"] = game_mode_parsed
        if game_mode_version is not UNSET:
            field_dict["game_mode_version"] = game_mode_version
        if lobby_id is not UNSET:
            field_dict["lobby_id"] = lobby_id
        if match_id is not UNSET:
            field_dict["match_id"] = match_id
        if match_mode is not UNSET:
            field_dict["match_mode"] = match_mode
        if match_mode_parsed is not UNSET:
            field_dict["match_mode_parsed"] = match_mode_parsed
        if match_score is not UNSET:
            field_dict["match_score"] = match_score
        if net_worth_team_0 is not UNSET:
            field_dict["net_worth_team_0"] = net_worth_team_0
        if net_worth_team_1 is not UNSET:
            field_dict["net_worth_team_1"] = net_worth_team_1
        if objectives_mask_team0 is not UNSET:
            field_dict["objectives_mask_team0"] = objectives_mask_team0
        if objectives_mask_team1 is not UNSET:
            field_dict["objectives_mask_team1"] = objectives_mask_team1
        if open_spectator_slots is not UNSET:
            field_dict["open_spectator_slots"] = open_spectator_slots
        if region_mode is not UNSET:
            field_dict["region_mode"] = region_mode
        if region_mode_parsed is not UNSET:
            field_dict["region_mode_parsed"] = region_mode_parsed
        if spectators is not UNSET:
            field_dict["spectators"] = spectators
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if winning_team is not UNSET:
            field_dict["winning_team"] = winning_team
        if winning_team_parsed is not UNSET:
            field_dict["winning_team_parsed"] = winning_team_parsed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.active_match_player import ActiveMatchPlayer

        d = dict(src_dict)
        players = []
        _players = d.pop("players")
        for players_item_data in _players:
            players_item = ActiveMatchPlayer.from_dict(players_item_data)

            players.append(players_item)

        def _parse_compat_version(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        compat_version = _parse_compat_version(d.pop("compat_version", UNSET))

        def _parse_duration_s(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        duration_s = _parse_duration_s(d.pop("duration_s", UNSET))

        def _parse_game_mode(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        game_mode = _parse_game_mode(d.pop("game_mode", UNSET))

        def _parse_game_mode_parsed(data: object) -> Union[ActiveMatchGameMode, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                game_mode_parsed_type_1 = ActiveMatchGameMode(data)

                return game_mode_parsed_type_1
            except:  # noqa: E722
                pass
            return cast(Union[ActiveMatchGameMode, None, Unset], data)

        game_mode_parsed = _parse_game_mode_parsed(d.pop("game_mode_parsed", UNSET))

        def _parse_game_mode_version(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        game_mode_version = _parse_game_mode_version(d.pop("game_mode_version", UNSET))

        def _parse_lobby_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        lobby_id = _parse_lobby_id(d.pop("lobby_id", UNSET))

        def _parse_match_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        match_id = _parse_match_id(d.pop("match_id", UNSET))

        def _parse_match_mode(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        match_mode = _parse_match_mode(d.pop("match_mode", UNSET))

        def _parse_match_mode_parsed(data: object) -> Union[ActiveMatchMode, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                match_mode_parsed_type_1 = ActiveMatchMode(data)

                return match_mode_parsed_type_1
            except:  # noqa: E722
                pass
            return cast(Union[ActiveMatchMode, None, Unset], data)

        match_mode_parsed = _parse_match_mode_parsed(d.pop("match_mode_parsed", UNSET))

        def _parse_match_score(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        match_score = _parse_match_score(d.pop("match_score", UNSET))

        def _parse_net_worth_team_0(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        net_worth_team_0 = _parse_net_worth_team_0(d.pop("net_worth_team_0", UNSET))

        def _parse_net_worth_team_1(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        net_worth_team_1 = _parse_net_worth_team_1(d.pop("net_worth_team_1", UNSET))

        def _parse_objectives_mask_team0(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        objectives_mask_team0 = _parse_objectives_mask_team0(d.pop("objectives_mask_team0", UNSET))

        def _parse_objectives_mask_team1(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        objectives_mask_team1 = _parse_objectives_mask_team1(d.pop("objectives_mask_team1", UNSET))

        def _parse_open_spectator_slots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        open_spectator_slots = _parse_open_spectator_slots(d.pop("open_spectator_slots", UNSET))

        def _parse_region_mode(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        region_mode = _parse_region_mode(d.pop("region_mode", UNSET))

        def _parse_region_mode_parsed(data: object) -> Union[ActiveMatchRegionMode, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                region_mode_parsed_type_1 = ActiveMatchRegionMode(data)

                return region_mode_parsed_type_1
            except:  # noqa: E722
                pass
            return cast(Union[ActiveMatchRegionMode, None, Unset], data)

        region_mode_parsed = _parse_region_mode_parsed(d.pop("region_mode_parsed", UNSET))

        def _parse_spectators(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        spectators = _parse_spectators(d.pop("spectators", UNSET))

        def _parse_start_time(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

        def _parse_winning_team(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        winning_team = _parse_winning_team(d.pop("winning_team", UNSET))

        def _parse_winning_team_parsed(data: object) -> Union[ActiveMatchTeam, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                winning_team_parsed_type_1 = ActiveMatchTeam(data)

                return winning_team_parsed_type_1
            except:  # noqa: E722
                pass
            return cast(Union[ActiveMatchTeam, None, Unset], data)

        winning_team_parsed = _parse_winning_team_parsed(d.pop("winning_team_parsed", UNSET))

        active_match = cls(
            players=players,
            compat_version=compat_version,
            duration_s=duration_s,
            game_mode=game_mode,
            game_mode_parsed=game_mode_parsed,
            game_mode_version=game_mode_version,
            lobby_id=lobby_id,
            match_id=match_id,
            match_mode=match_mode,
            match_mode_parsed=match_mode_parsed,
            match_score=match_score,
            net_worth_team_0=net_worth_team_0,
            net_worth_team_1=net_worth_team_1,
            objectives_mask_team0=objectives_mask_team0,
            objectives_mask_team1=objectives_mask_team1,
            open_spectator_slots=open_spectator_slots,
            region_mode=region_mode,
            region_mode_parsed=region_mode_parsed,
            spectators=spectators,
            start_time=start_time,
            winning_team=winning_team,
            winning_team_parsed=winning_team_parsed,
        )

        active_match.additional_properties = d
        return active_match

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
