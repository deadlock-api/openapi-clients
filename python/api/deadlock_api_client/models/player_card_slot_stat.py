from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerCardSlotStat")


@_attrs_define
class PlayerCardSlotStat:
    """
    Attributes:
        stat_id (Union[None, Unset, int]):
        stat_score (Union[None, Unset, int]):
    """

    stat_id: Union[None, Unset, int] = UNSET
    stat_score: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stat_id: Union[None, Unset, int]
        if isinstance(self.stat_id, Unset):
            stat_id = UNSET
        else:
            stat_id = self.stat_id

        stat_score: Union[None, Unset, int]
        if isinstance(self.stat_score, Unset):
            stat_score = UNSET
        else:
            stat_score = self.stat_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stat_id is not UNSET:
            field_dict["stat_id"] = stat_id
        if stat_score is not UNSET:
            field_dict["stat_score"] = stat_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_stat_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        stat_id = _parse_stat_id(d.pop("stat_id", UNSET))

        def _parse_stat_score(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        stat_score = _parse_stat_score(d.pop("stat_score", UNSET))

        player_card_slot_stat = cls(
            stat_id=stat_id,
            stat_score=stat_score,
        )

        player_card_slot_stat.additional_properties = d
        return player_card_slot_stat

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
