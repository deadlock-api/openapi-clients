from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeroShopWeaponStatsDisplayV2")


@_attrs_define
class HeroShopWeaponStatsDisplayV2:
    """
    Attributes:
        display_stats (list[str]):
        other_display_stats (list[str]):
        weapon_attributes (Union[None, Unset, list[str]]):
        weapon_image (Union[None, Unset, str]):
        weapon_image_webp (Union[None, Unset, str]):
    """

    display_stats: list[str]
    other_display_stats: list[str]
    weapon_attributes: Union[None, Unset, list[str]] = UNSET
    weapon_image: Union[None, Unset, str] = UNSET
    weapon_image_webp: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_stats = self.display_stats

        other_display_stats = self.other_display_stats

        weapon_attributes: Union[None, Unset, list[str]]
        if isinstance(self.weapon_attributes, Unset):
            weapon_attributes = UNSET
        elif isinstance(self.weapon_attributes, list):
            weapon_attributes = self.weapon_attributes

        else:
            weapon_attributes = self.weapon_attributes

        weapon_image: Union[None, Unset, str]
        if isinstance(self.weapon_image, Unset):
            weapon_image = UNSET
        else:
            weapon_image = self.weapon_image

        weapon_image_webp: Union[None, Unset, str]
        if isinstance(self.weapon_image_webp, Unset):
            weapon_image_webp = UNSET
        else:
            weapon_image_webp = self.weapon_image_webp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display_stats": display_stats,
                "other_display_stats": other_display_stats,
            }
        )
        if weapon_attributes is not UNSET:
            field_dict["weapon_attributes"] = weapon_attributes
        if weapon_image is not UNSET:
            field_dict["weapon_image"] = weapon_image
        if weapon_image_webp is not UNSET:
            field_dict["weapon_image_webp"] = weapon_image_webp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_stats = cast(list[str], d.pop("display_stats"))

        other_display_stats = cast(list[str], d.pop("other_display_stats"))

        def _parse_weapon_attributes(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                weapon_attributes_type_0 = cast(list[str], data)

                return weapon_attributes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        weapon_attributes = _parse_weapon_attributes(d.pop("weapon_attributes", UNSET))

        def _parse_weapon_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        weapon_image = _parse_weapon_image(d.pop("weapon_image", UNSET))

        def _parse_weapon_image_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        weapon_image_webp = _parse_weapon_image_webp(d.pop("weapon_image_webp", UNSET))

        hero_shop_weapon_stats_display_v2 = cls(
            display_stats=display_stats,
            other_display_stats=other_display_stats,
            weapon_attributes=weapon_attributes,
            weapon_image=weapon_image,
            weapon_image_webp=weapon_image_webp,
        )

        hero_shop_weapon_stats_display_v2.additional_properties = d
        return hero_shop_weapon_stats_display_v2

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
