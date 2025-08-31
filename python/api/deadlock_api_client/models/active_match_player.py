from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.active_match_team import ActiveMatchTeam
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActiveMatchPlayer")


@_attrs_define
class ActiveMatchPlayer:
    """
    Attributes:
        abandoned (Union[None, Unset, bool]):
        account_id (Union[None, Unset, int]):
        hero_id (Union[None, Unset, int]): See more: <https://assets.deadlock-api.com/v2/heroes>
        team (Union[None, Unset, int]):
        team_parsed (Union[ActiveMatchTeam, None, Unset]):
    """

    abandoned: Union[None, Unset, bool] = UNSET
    account_id: Union[None, Unset, int] = UNSET
    hero_id: Union[None, Unset, int] = UNSET
    team: Union[None, Unset, int] = UNSET
    team_parsed: Union[ActiveMatchTeam, None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abandoned: Union[None, Unset, bool]
        if isinstance(self.abandoned, Unset):
            abandoned = UNSET
        else:
            abandoned = self.abandoned

        account_id: Union[None, Unset, int]
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        hero_id: Union[None, Unset, int]
        if isinstance(self.hero_id, Unset):
            hero_id = UNSET
        else:
            hero_id = self.hero_id

        team: Union[None, Unset, int]
        if isinstance(self.team, Unset):
            team = UNSET
        else:
            team = self.team

        team_parsed: Union[None, Unset, str]
        if isinstance(self.team_parsed, Unset):
            team_parsed = UNSET
        elif isinstance(self.team_parsed, ActiveMatchTeam):
            team_parsed = self.team_parsed.value
        else:
            team_parsed = self.team_parsed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abandoned is not UNSET:
            field_dict["abandoned"] = abandoned
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if hero_id is not UNSET:
            field_dict["hero_id"] = hero_id
        if team is not UNSET:
            field_dict["team"] = team
        if team_parsed is not UNSET:
            field_dict["team_parsed"] = team_parsed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_abandoned(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        abandoned = _parse_abandoned(d.pop("abandoned", UNSET))

        def _parse_account_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))

        def _parse_hero_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        hero_id = _parse_hero_id(d.pop("hero_id", UNSET))

        def _parse_team(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        team = _parse_team(d.pop("team", UNSET))

        def _parse_team_parsed(data: object) -> Union[ActiveMatchTeam, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                team_parsed_type_1 = ActiveMatchTeam(data)

                return team_parsed_type_1
            except:  # noqa: E722
                pass
            return cast(Union[ActiveMatchTeam, None, Unset], data)

        team_parsed = _parse_team_parsed(d.pop("team_parsed", UNSET))

        active_match_player = cls(
            abandoned=abandoned,
            account_id=account_id,
            hero_id=hero_id,
            team=team,
            team_parsed=team_parsed,
        )

        active_match_player.additional_properties = d
        return active_match_player

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
