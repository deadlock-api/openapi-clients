from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClickhouseMatchInfo")


@_attrs_define
class ClickhouseMatchInfo:
    """
    Attributes:
        duration_s (int):
        match_id (int):
        match_mode (int):
        start_time (int):
        average_badge_team0 (Union[None, Unset, int]): See more: <https://assets.deadlock-api.com/v2/ranks>
        average_badge_team1 (Union[None, Unset, int]): See more: <https://assets.deadlock-api.com/v2/ranks>
    """

    duration_s: int
    match_id: int
    match_mode: int
    start_time: int
    average_badge_team0: Union[None, Unset, int] = UNSET
    average_badge_team1: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_s = self.duration_s

        match_id = self.match_id

        match_mode = self.match_mode

        start_time = self.start_time

        average_badge_team0: Union[None, Unset, int]
        if isinstance(self.average_badge_team0, Unset):
            average_badge_team0 = UNSET
        else:
            average_badge_team0 = self.average_badge_team0

        average_badge_team1: Union[None, Unset, int]
        if isinstance(self.average_badge_team1, Unset):
            average_badge_team1 = UNSET
        else:
            average_badge_team1 = self.average_badge_team1

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration_s": duration_s,
                "match_id": match_id,
                "match_mode": match_mode,
                "start_time": start_time,
            }
        )
        if average_badge_team0 is not UNSET:
            field_dict["average_badge_team0"] = average_badge_team0
        if average_badge_team1 is not UNSET:
            field_dict["average_badge_team1"] = average_badge_team1

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration_s = d.pop("duration_s")

        match_id = d.pop("match_id")

        match_mode = d.pop("match_mode")

        start_time = d.pop("start_time")

        def _parse_average_badge_team0(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        average_badge_team0 = _parse_average_badge_team0(d.pop("average_badge_team0", UNSET))

        def _parse_average_badge_team1(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        average_badge_team1 = _parse_average_badge_team1(d.pop("average_badge_team1", UNSET))

        clickhouse_match_info = cls(
            duration_s=duration_s,
            match_id=match_id,
            match_mode=match_mode,
            start_time=start_time,
            average_badge_team0=average_badge_team0,
            average_badge_team1=average_badge_team1,
        )

        clickhouse_match_info.additional_properties = d
        return clickhouse_match_info

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
