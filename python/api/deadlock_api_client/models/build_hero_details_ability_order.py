from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.build_hero_details_ability_order_currency_change import BuildHeroDetailsAbilityOrderCurrencyChange


T = TypeVar("T", bound="BuildHeroDetailsAbilityOrder")


@_attrs_define
class BuildHeroDetailsAbilityOrder:
    """
    Attributes:
        currency_changes (Union[None, Unset, list['BuildHeroDetailsAbilityOrderCurrencyChange']]):
    """

    currency_changes: Union[None, Unset, list["BuildHeroDetailsAbilityOrderCurrencyChange"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_changes: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.currency_changes, Unset):
            currency_changes = UNSET
        elif isinstance(self.currency_changes, list):
            currency_changes = []
            for currency_changes_type_0_item_data in self.currency_changes:
                currency_changes_type_0_item = currency_changes_type_0_item_data.to_dict()
                currency_changes.append(currency_changes_type_0_item)

        else:
            currency_changes = self.currency_changes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_changes is not UNSET:
            field_dict["currency_changes"] = currency_changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.build_hero_details_ability_order_currency_change import BuildHeroDetailsAbilityOrderCurrencyChange

        d = dict(src_dict)

        def _parse_currency_changes(
            data: object,
        ) -> Union[None, Unset, list["BuildHeroDetailsAbilityOrderCurrencyChange"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                currency_changes_type_0 = []
                _currency_changes_type_0 = data
                for currency_changes_type_0_item_data in _currency_changes_type_0:
                    currency_changes_type_0_item = BuildHeroDetailsAbilityOrderCurrencyChange.from_dict(
                        currency_changes_type_0_item_data
                    )

                    currency_changes_type_0.append(currency_changes_type_0_item)

                return currency_changes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["BuildHeroDetailsAbilityOrderCurrencyChange"]], data)

        currency_changes = _parse_currency_changes(d.pop("currency_changes", UNSET))

        build_hero_details_ability_order = cls(
            currency_changes=currency_changes,
        )

        build_hero_details_ability_order.additional_properties = d
        return build_hero_details_ability_order

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
