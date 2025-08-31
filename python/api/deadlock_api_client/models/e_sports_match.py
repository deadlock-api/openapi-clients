import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.e_sports_match_status import ESportsMatchStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ESportsMatch")


@_attrs_define
class ESportsMatch:
    """
    Attributes:
        provider (str): The provider of the match data. Some string that identifies the source of the data.
        match_id (Union[None, Unset, int]): Valve's match id of the match.
        scheduled_date (Union[None, Unset, datetime.datetime]): The scheduled date of the match.
        status (Union[ESportsMatchStatus, None, Unset]):
        team0_name (Union[None, Unset, str]): The name of the first team.
        team1_name (Union[None, Unset, str]): The name of the second team.
        tournament_name (Union[None, Unset, str]): The name of the tournament.
        tournament_stage (Union[None, Unset, str]): The stage of the tournament.
        update_id (Union[None, UUID, Unset]): If you want to update an existing match, you can provide an update id.
    """

    provider: str
    match_id: Union[None, Unset, int] = UNSET
    scheduled_date: Union[None, Unset, datetime.datetime] = UNSET
    status: Union[ESportsMatchStatus, None, Unset] = UNSET
    team0_name: Union[None, Unset, str] = UNSET
    team1_name: Union[None, Unset, str] = UNSET
    tournament_name: Union[None, Unset, str] = UNSET
    tournament_stage: Union[None, Unset, str] = UNSET
    update_id: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        match_id: Union[None, Unset, int]
        if isinstance(self.match_id, Unset):
            match_id = UNSET
        else:
            match_id = self.match_id

        scheduled_date: Union[None, Unset, str]
        if isinstance(self.scheduled_date, Unset):
            scheduled_date = UNSET
        elif isinstance(self.scheduled_date, datetime.datetime):
            scheduled_date = self.scheduled_date.isoformat()
        else:
            scheduled_date = self.scheduled_date

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, ESportsMatchStatus):
            status = self.status.value
        else:
            status = self.status

        team0_name: Union[None, Unset, str]
        if isinstance(self.team0_name, Unset):
            team0_name = UNSET
        else:
            team0_name = self.team0_name

        team1_name: Union[None, Unset, str]
        if isinstance(self.team1_name, Unset):
            team1_name = UNSET
        else:
            team1_name = self.team1_name

        tournament_name: Union[None, Unset, str]
        if isinstance(self.tournament_name, Unset):
            tournament_name = UNSET
        else:
            tournament_name = self.tournament_name

        tournament_stage: Union[None, Unset, str]
        if isinstance(self.tournament_stage, Unset):
            tournament_stage = UNSET
        else:
            tournament_stage = self.tournament_stage

        update_id: Union[None, Unset, str]
        if isinstance(self.update_id, Unset):
            update_id = UNSET
        elif isinstance(self.update_id, UUID):
            update_id = str(self.update_id)
        else:
            update_id = self.update_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if match_id is not UNSET:
            field_dict["match_id"] = match_id
        if scheduled_date is not UNSET:
            field_dict["scheduled_date"] = scheduled_date
        if status is not UNSET:
            field_dict["status"] = status
        if team0_name is not UNSET:
            field_dict["team0_name"] = team0_name
        if team1_name is not UNSET:
            field_dict["team1_name"] = team1_name
        if tournament_name is not UNSET:
            field_dict["tournament_name"] = tournament_name
        if tournament_stage is not UNSET:
            field_dict["tournament_stage"] = tournament_stage
        if update_id is not UNSET:
            field_dict["update_id"] = update_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = d.pop("provider")

        def _parse_match_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        match_id = _parse_match_id(d.pop("match_id", UNSET))

        def _parse_scheduled_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_date_type_0 = isoparse(data)

                return scheduled_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        scheduled_date = _parse_scheduled_date(d.pop("scheduled_date", UNSET))

        def _parse_status(data: object) -> Union[ESportsMatchStatus, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = ESportsMatchStatus(data)

                return status_type_1
            except:  # noqa: E722
                pass
            return cast(Union[ESportsMatchStatus, None, Unset], data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_team0_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        team0_name = _parse_team0_name(d.pop("team0_name", UNSET))

        def _parse_team1_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        team1_name = _parse_team1_name(d.pop("team1_name", UNSET))

        def _parse_tournament_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tournament_name = _parse_tournament_name(d.pop("tournament_name", UNSET))

        def _parse_tournament_stage(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tournament_stage = _parse_tournament_stage(d.pop("tournament_stage", UNSET))

        def _parse_update_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_id_type_0 = UUID(data)

                return update_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        update_id = _parse_update_id(d.pop("update_id", UNSET))

        e_sports_match = cls(
            provider=provider,
            match_id=match_id,
            scheduled_date=scheduled_date,
            status=status,
            team0_name=team0_name,
            team1_name=team1_name,
            tournament_name=tournament_name,
            tournament_stage=tournament_stage,
            update_id=update_id,
        )

        e_sports_match.additional_properties = d
        return e_sports_match

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
