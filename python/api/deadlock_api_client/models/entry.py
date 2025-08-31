from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Entry")


@_attrs_define
class Entry:
    """
    Attributes:
        hero_id (int): See more: <https://assets.deadlock-api.com/v2/heroes>
        matches (int):
        rank (int): See more: <https://assets.deadlock-api.com/v2/ranks>
        value (float):
    """

    hero_id: int
    matches: int
    rank: int
    value: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hero_id = self.hero_id

        matches = self.matches

        rank = self.rank

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hero_id": hero_id,
                "matches": matches,
                "rank": rank,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hero_id = d.pop("hero_id")

        matches = d.pop("matches")

        rank = d.pop("rank")

        value = d.pop("value")

        entry = cls(
            hero_id=hero_id,
            matches=matches,
            rank=rank,
            value=value,
        )

        entry.additional_properties = d
        return entry

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
