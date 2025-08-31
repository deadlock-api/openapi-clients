from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeroDescriptionV2")


@_attrs_define
class HeroDescriptionV2:
    """
    Attributes:
        lore (Union[None, Unset, str]):
        role (Union[None, Unset, str]):
        playstyle (Union[None, Unset, str]):
    """

    lore: Union[None, Unset, str] = UNSET
    role: Union[None, Unset, str] = UNSET
    playstyle: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lore: Union[None, Unset, str]
        if isinstance(self.lore, Unset):
            lore = UNSET
        else:
            lore = self.lore

        role: Union[None, Unset, str]
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        playstyle: Union[None, Unset, str]
        if isinstance(self.playstyle, Unset):
            playstyle = UNSET
        else:
            playstyle = self.playstyle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lore is not UNSET:
            field_dict["lore"] = lore
        if role is not UNSET:
            field_dict["role"] = role
        if playstyle is not UNSET:
            field_dict["playstyle"] = playstyle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_lore(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        lore = _parse_lore(d.pop("lore", UNSET))

        def _parse_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_playstyle(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        playstyle = _parse_playstyle(d.pop("playstyle", UNSET))

        hero_description_v2 = cls(
            lore=lore,
            role=role,
            playstyle=playstyle,
        )

        hero_description_v2.additional_properties = d
        return hero_description_v2

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
