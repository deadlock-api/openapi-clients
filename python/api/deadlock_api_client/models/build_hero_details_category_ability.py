from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuildHeroDetailsCategoryAbility")


@_attrs_define
class BuildHeroDetailsCategoryAbility:
    """
    Attributes:
        ability_id (int):
        annotation (Union[None, Unset, str]):
        imbue_target_ability_id (Union[None, Unset, int]):
        required_flex_slots (Union[None, Unset, int]):
        sell_priority (Union[None, Unset, int]):
    """

    ability_id: int
    annotation: Union[None, Unset, str] = UNSET
    imbue_target_ability_id: Union[None, Unset, int] = UNSET
    required_flex_slots: Union[None, Unset, int] = UNSET
    sell_priority: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ability_id = self.ability_id

        annotation: Union[None, Unset, str]
        if isinstance(self.annotation, Unset):
            annotation = UNSET
        else:
            annotation = self.annotation

        imbue_target_ability_id: Union[None, Unset, int]
        if isinstance(self.imbue_target_ability_id, Unset):
            imbue_target_ability_id = UNSET
        else:
            imbue_target_ability_id = self.imbue_target_ability_id

        required_flex_slots: Union[None, Unset, int]
        if isinstance(self.required_flex_slots, Unset):
            required_flex_slots = UNSET
        else:
            required_flex_slots = self.required_flex_slots

        sell_priority: Union[None, Unset, int]
        if isinstance(self.sell_priority, Unset):
            sell_priority = UNSET
        else:
            sell_priority = self.sell_priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ability_id": ability_id,
            }
        )
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if imbue_target_ability_id is not UNSET:
            field_dict["imbue_target_ability_id"] = imbue_target_ability_id
        if required_flex_slots is not UNSET:
            field_dict["required_flex_slots"] = required_flex_slots
        if sell_priority is not UNSET:
            field_dict["sell_priority"] = sell_priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ability_id = d.pop("ability_id")

        def _parse_annotation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        annotation = _parse_annotation(d.pop("annotation", UNSET))

        def _parse_imbue_target_ability_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        imbue_target_ability_id = _parse_imbue_target_ability_id(d.pop("imbue_target_ability_id", UNSET))

        def _parse_required_flex_slots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        required_flex_slots = _parse_required_flex_slots(d.pop("required_flex_slots", UNSET))

        def _parse_sell_priority(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sell_priority = _parse_sell_priority(d.pop("sell_priority", UNSET))

        build_hero_details_category_ability = cls(
            ability_id=ability_id,
            annotation=annotation,
            imbue_target_ability_id=imbue_target_ability_id,
            required_flex_slots=required_flex_slots,
            sell_priority=sell_priority,
        )

        build_hero_details_category_ability.additional_properties = d
        return build_hero_details_category_ability

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
