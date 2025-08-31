from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpgradeDescriptionV2")


@_attrs_define
class UpgradeDescriptionV2:
    """
    Attributes:
        desc (Union[None, Unset, str]):
        active (Union[None, Unset, str]):
        passive (Union[None, Unset, str]):
    """

    desc: Union[None, Unset, str] = UNSET
    active: Union[None, Unset, str] = UNSET
    passive: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        desc: Union[None, Unset, str]
        if isinstance(self.desc, Unset):
            desc = UNSET
        else:
            desc = self.desc

        active: Union[None, Unset, str]
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        passive: Union[None, Unset, str]
        if isinstance(self.passive, Unset):
            passive = UNSET
        else:
            passive = self.passive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if desc is not UNSET:
            field_dict["desc"] = desc
        if active is not UNSET:
            field_dict["active"] = active
        if passive is not UNSET:
            field_dict["passive"] = passive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_desc(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        desc = _parse_desc(d.pop("desc", UNSET))

        def _parse_active(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_passive(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        passive = _parse_passive(d.pop("passive", UNSET))

        upgrade_description_v2 = cls(
            desc=desc,
            active=active,
            passive=passive,
        )

        upgrade_description_v2.additional_properties = d
        return upgrade_description_v2

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
