from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RawAbilityUpgradePropertyUpgradeV2")


@_attrs_define
class RawAbilityUpgradePropertyUpgradeV2:
    """
    Attributes:
        name (str):
        bonus (Union[float, str]):
        scale_stat_filter (Union[None, Unset, str]):
        upgrade_type (Union[None, Unset, str]):
    """

    name: str
    bonus: Union[float, str]
    scale_stat_filter: Union[None, Unset, str] = UNSET
    upgrade_type: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        bonus: Union[float, str]
        bonus = self.bonus

        scale_stat_filter: Union[None, Unset, str]
        if isinstance(self.scale_stat_filter, Unset):
            scale_stat_filter = UNSET
        else:
            scale_stat_filter = self.scale_stat_filter

        upgrade_type: Union[None, Unset, str]
        if isinstance(self.upgrade_type, Unset):
            upgrade_type = UNSET
        else:
            upgrade_type = self.upgrade_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "bonus": bonus,
            }
        )
        if scale_stat_filter is not UNSET:
            field_dict["scale_stat_filter"] = scale_stat_filter
        if upgrade_type is not UNSET:
            field_dict["upgrade_type"] = upgrade_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_bonus(data: object) -> Union[float, str]:
            return cast(Union[float, str], data)

        bonus = _parse_bonus(d.pop("bonus"))

        def _parse_scale_stat_filter(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scale_stat_filter = _parse_scale_stat_filter(d.pop("scale_stat_filter", UNSET))

        def _parse_upgrade_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        upgrade_type = _parse_upgrade_type(d.pop("upgrade_type", UNSET))

        raw_ability_upgrade_property_upgrade_v2 = cls(
            name=name,
            bonus=bonus,
            scale_stat_filter=scale_stat_filter,
            upgrade_type=upgrade_type,
        )

        raw_ability_upgrade_property_upgrade_v2.additional_properties = d
        return raw_ability_upgrade_property_upgrade_v2

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
