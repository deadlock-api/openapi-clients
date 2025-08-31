from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MMRHistory")


@_attrs_define
class MMRHistory:
    """
    Attributes:
        account_id (int):
        division (int): Extracted from the rank the division (rank // 10)
        division_tier (int): Extracted from the rank the division tier (rank % 10)
        match_id (int):
        player_score (float): Player Score is the index for the rank array (internally used for the rank regression)
        rank (int): The Player Rank. See more: <https://assets.deadlock-api.com/v2/ranks>
        start_time (int): Start time of the match
    """

    account_id: int
    division: int
    division_tier: int
    match_id: int
    player_score: float
    rank: int
    start_time: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        division = self.division

        division_tier = self.division_tier

        match_id = self.match_id

        player_score = self.player_score

        rank = self.rank

        start_time = self.start_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "division": division,
                "division_tier": division_tier,
                "match_id": match_id,
                "player_score": player_score,
                "rank": rank,
                "start_time": start_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        division = d.pop("division")

        division_tier = d.pop("division_tier")

        match_id = d.pop("match_id")

        player_score = d.pop("player_score")

        rank = d.pop("rank")

        start_time = d.pop("start_time")

        mmr_history = cls(
            account_id=account_id,
            division=division,
            division_tier=division_tier,
            match_id=match_id,
            player_score=player_score,
            rank=rank,
            start_time=start_time,
        )

        mmr_history.additional_properties = d
        return mmr_history

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
