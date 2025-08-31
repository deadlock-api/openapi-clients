from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.build_hero_details_ability_order import BuildHeroDetailsAbilityOrder
    from ..models.build_hero_details_category import BuildHeroDetailsCategory


T = TypeVar("T", bound="BuildHeroDetails")


@_attrs_define
class BuildHeroDetails:
    """
    Attributes:
        mod_categories (list['BuildHeroDetailsCategory']):
        ability_order (Union['BuildHeroDetailsAbilityOrder', None, Unset]):
    """

    mod_categories: list["BuildHeroDetailsCategory"]
    ability_order: Union["BuildHeroDetailsAbilityOrder", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.build_hero_details_ability_order import BuildHeroDetailsAbilityOrder

        mod_categories = []
        for mod_categories_item_data in self.mod_categories:
            mod_categories_item = mod_categories_item_data.to_dict()
            mod_categories.append(mod_categories_item)

        ability_order: Union[None, Unset, dict[str, Any]]
        if isinstance(self.ability_order, Unset):
            ability_order = UNSET
        elif isinstance(self.ability_order, BuildHeroDetailsAbilityOrder):
            ability_order = self.ability_order.to_dict()
        else:
            ability_order = self.ability_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mod_categories": mod_categories,
            }
        )
        if ability_order is not UNSET:
            field_dict["ability_order"] = ability_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.build_hero_details_ability_order import BuildHeroDetailsAbilityOrder
        from ..models.build_hero_details_category import BuildHeroDetailsCategory

        d = dict(src_dict)
        mod_categories = []
        _mod_categories = d.pop("mod_categories")
        for mod_categories_item_data in _mod_categories:
            mod_categories_item = BuildHeroDetailsCategory.from_dict(mod_categories_item_data)

            mod_categories.append(mod_categories_item)

        def _parse_ability_order(data: object) -> Union["BuildHeroDetailsAbilityOrder", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ability_order_type_1 = BuildHeroDetailsAbilityOrder.from_dict(data)

                return ability_order_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BuildHeroDetailsAbilityOrder", None, Unset], data)

        ability_order = _parse_ability_order(d.pop("ability_order", UNSET))

        build_hero_details = cls(
            mod_categories=mod_categories,
            ability_order=ability_order,
        )

        build_hero_details.additional_properties = d
        return build_hero_details

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
