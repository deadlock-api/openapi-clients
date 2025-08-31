from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BadgeDistribution")


@_attrs_define
class BadgeDistribution:
    """
    Attributes:
        badge_level (int): The badge level. See more: <https://assets.deadlock-api.com/v2/ranks>
        total_matches (int): The total number of matches.
    """

    badge_level: int
    total_matches: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        badge_level = self.badge_level

        total_matches = self.total_matches

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "badge_level": badge_level,
                "total_matches": total_matches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        badge_level = d.pop("badge_level")

        total_matches = d.pop("total_matches")

        badge_distribution = cls(
            badge_level=badge_level,
            total_matches=total_matches,
        )

        badge_distribution.additional_properties = d
        return badge_distribution

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
