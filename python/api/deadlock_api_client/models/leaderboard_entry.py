from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LeaderboardEntry")


@_attrs_define
class LeaderboardEntry:
    """
    Attributes:
        account_name (Union[None, Unset, str]): The account name of the player.
        badge_level (Union[None, Unset, int]): The badge level of the player. See more: <https://assets.deadlock-
            api.com/v2/ranks>
        possible_account_ids (Union[Unset, list[int]]): The possible account IDs of the player. **CAVEAT: This is not
            always correct, as Steam account names are not unique.**
        rank (Union[None, Unset, int]): The rank of the player. See more: <https://assets.deadlock-api.com/v2/ranks>
        ranked_rank (Union[None, Unset, int]): The ranked rank of the player. See more: <https://assets.deadlock-
            api.com/v2/ranks>
        ranked_subrank (Union[None, Unset, int]): The ranked subrank of the player. See more: <https://assets.deadlock-
            api.com/v2/ranks>
        top_hero_ids (Union[Unset, list[int]]): The top hero IDs of the player. See more: <https://assets.deadlock-
            api.com/v2/heroes>
    """

    account_name: Union[None, Unset, str] = UNSET
    badge_level: Union[None, Unset, int] = UNSET
    possible_account_ids: Union[Unset, list[int]] = UNSET
    rank: Union[None, Unset, int] = UNSET
    ranked_rank: Union[None, Unset, int] = UNSET
    ranked_subrank: Union[None, Unset, int] = UNSET
    top_hero_ids: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_name: Union[None, Unset, str]
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name

        badge_level: Union[None, Unset, int]
        if isinstance(self.badge_level, Unset):
            badge_level = UNSET
        else:
            badge_level = self.badge_level

        possible_account_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.possible_account_ids, Unset):
            possible_account_ids = self.possible_account_ids

        rank: Union[None, Unset, int]
        if isinstance(self.rank, Unset):
            rank = UNSET
        else:
            rank = self.rank

        ranked_rank: Union[None, Unset, int]
        if isinstance(self.ranked_rank, Unset):
            ranked_rank = UNSET
        else:
            ranked_rank = self.ranked_rank

        ranked_subrank: Union[None, Unset, int]
        if isinstance(self.ranked_subrank, Unset):
            ranked_subrank = UNSET
        else:
            ranked_subrank = self.ranked_subrank

        top_hero_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.top_hero_ids, Unset):
            top_hero_ids = self.top_hero_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if badge_level is not UNSET:
            field_dict["badge_level"] = badge_level
        if possible_account_ids is not UNSET:
            field_dict["possible_account_ids"] = possible_account_ids
        if rank is not UNSET:
            field_dict["rank"] = rank
        if ranked_rank is not UNSET:
            field_dict["ranked_rank"] = ranked_rank
        if ranked_subrank is not UNSET:
            field_dict["ranked_subrank"] = ranked_subrank
        if top_hero_ids is not UNSET:
            field_dict["top_hero_ids"] = top_hero_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_account_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        account_name = _parse_account_name(d.pop("account_name", UNSET))

        def _parse_badge_level(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        badge_level = _parse_badge_level(d.pop("badge_level", UNSET))

        possible_account_ids = cast(list[int], d.pop("possible_account_ids", UNSET))

        def _parse_rank(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rank = _parse_rank(d.pop("rank", UNSET))

        def _parse_ranked_rank(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        ranked_rank = _parse_ranked_rank(d.pop("ranked_rank", UNSET))

        def _parse_ranked_subrank(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        ranked_subrank = _parse_ranked_subrank(d.pop("ranked_subrank", UNSET))

        top_hero_ids = cast(list[int], d.pop("top_hero_ids", UNSET))

        leaderboard_entry = cls(
            account_name=account_name,
            badge_level=badge_level,
            possible_account_ids=possible_account_ids,
            rank=rank,
            ranked_rank=ranked_rank,
            ranked_subrank=ranked_subrank,
            top_hero_ids=top_hero_ids,
        )

        leaderboard_entry.additional_properties = d
        return leaderboard_entry

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
