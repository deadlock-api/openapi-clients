from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeroLevelInfoV2")


@_attrs_define
class HeroLevelInfoV2:
    """
    Attributes:
        required_gold (int):
        use_standard_upgrade (Union[None, Unset, bool]):
        bonus_currencies (Union[None, Unset, list[str]]):
    """

    required_gold: int
    use_standard_upgrade: Union[None, Unset, bool] = UNSET
    bonus_currencies: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        required_gold = self.required_gold

        use_standard_upgrade: Union[None, Unset, bool]
        if isinstance(self.use_standard_upgrade, Unset):
            use_standard_upgrade = UNSET
        else:
            use_standard_upgrade = self.use_standard_upgrade

        bonus_currencies: Union[None, Unset, list[str]]
        if isinstance(self.bonus_currencies, Unset):
            bonus_currencies = UNSET
        elif isinstance(self.bonus_currencies, list):
            bonus_currencies = self.bonus_currencies

        else:
            bonus_currencies = self.bonus_currencies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "required_gold": required_gold,
            }
        )
        if use_standard_upgrade is not UNSET:
            field_dict["use_standard_upgrade"] = use_standard_upgrade
        if bonus_currencies is not UNSET:
            field_dict["bonus_currencies"] = bonus_currencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        required_gold = d.pop("required_gold")

        def _parse_use_standard_upgrade(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        use_standard_upgrade = _parse_use_standard_upgrade(d.pop("use_standard_upgrade", UNSET))

        def _parse_bonus_currencies(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bonus_currencies_type_0 = cast(list[str], data)

                return bonus_currencies_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        bonus_currencies = _parse_bonus_currencies(d.pop("bonus_currencies", UNSET))

        hero_level_info_v2 = cls(
            required_gold=required_gold,
            use_standard_upgrade=use_standard_upgrade,
            bonus_currencies=bonus_currencies,
        )

        hero_level_info_v2.additional_properties = d
        return hero_level_info_v2

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
