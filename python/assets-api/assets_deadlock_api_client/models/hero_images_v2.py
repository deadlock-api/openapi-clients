from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeroImagesV2")


@_attrs_define
class HeroImagesV2:
    """
    Attributes:
        icon_hero_card (Union[None, Unset, str]):
        icon_hero_card_webp (Union[None, Unset, str]):
        icon_image_small (Union[None, Unset, str]):
        icon_image_small_webp (Union[None, Unset, str]):
        minimap_image (Union[None, Unset, str]):
        minimap_image_webp (Union[None, Unset, str]):
        selection_image (Union[None, Unset, str]):
        selection_image_webp (Union[None, Unset, str]):
        top_bar_image (Union[None, Unset, str]):
        top_bar_image_webp (Union[None, Unset, str]):
        top_bar_vertical_image (Union[None, Unset, str]):
        top_bar_vertical_image_webp (Union[None, Unset, str]):
        weapon_image (Union[None, Unset, str]):
        weapon_image_webp (Union[None, Unset, str]):
        background_image (Union[None, Unset, str]):
        background_image_webp (Union[None, Unset, str]):
        name_image (Union[None, Unset, str]):
    """

    icon_hero_card: Union[None, Unset, str] = UNSET
    icon_hero_card_webp: Union[None, Unset, str] = UNSET
    icon_image_small: Union[None, Unset, str] = UNSET
    icon_image_small_webp: Union[None, Unset, str] = UNSET
    minimap_image: Union[None, Unset, str] = UNSET
    minimap_image_webp: Union[None, Unset, str] = UNSET
    selection_image: Union[None, Unset, str] = UNSET
    selection_image_webp: Union[None, Unset, str] = UNSET
    top_bar_image: Union[None, Unset, str] = UNSET
    top_bar_image_webp: Union[None, Unset, str] = UNSET
    top_bar_vertical_image: Union[None, Unset, str] = UNSET
    top_bar_vertical_image_webp: Union[None, Unset, str] = UNSET
    weapon_image: Union[None, Unset, str] = UNSET
    weapon_image_webp: Union[None, Unset, str] = UNSET
    background_image: Union[None, Unset, str] = UNSET
    background_image_webp: Union[None, Unset, str] = UNSET
    name_image: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        icon_hero_card: Union[None, Unset, str]
        if isinstance(self.icon_hero_card, Unset):
            icon_hero_card = UNSET
        else:
            icon_hero_card = self.icon_hero_card

        icon_hero_card_webp: Union[None, Unset, str]
        if isinstance(self.icon_hero_card_webp, Unset):
            icon_hero_card_webp = UNSET
        else:
            icon_hero_card_webp = self.icon_hero_card_webp

        icon_image_small: Union[None, Unset, str]
        if isinstance(self.icon_image_small, Unset):
            icon_image_small = UNSET
        else:
            icon_image_small = self.icon_image_small

        icon_image_small_webp: Union[None, Unset, str]
        if isinstance(self.icon_image_small_webp, Unset):
            icon_image_small_webp = UNSET
        else:
            icon_image_small_webp = self.icon_image_small_webp

        minimap_image: Union[None, Unset, str]
        if isinstance(self.minimap_image, Unset):
            minimap_image = UNSET
        else:
            minimap_image = self.minimap_image

        minimap_image_webp: Union[None, Unset, str]
        if isinstance(self.minimap_image_webp, Unset):
            minimap_image_webp = UNSET
        else:
            minimap_image_webp = self.minimap_image_webp

        selection_image: Union[None, Unset, str]
        if isinstance(self.selection_image, Unset):
            selection_image = UNSET
        else:
            selection_image = self.selection_image

        selection_image_webp: Union[None, Unset, str]
        if isinstance(self.selection_image_webp, Unset):
            selection_image_webp = UNSET
        else:
            selection_image_webp = self.selection_image_webp

        top_bar_image: Union[None, Unset, str]
        if isinstance(self.top_bar_image, Unset):
            top_bar_image = UNSET
        else:
            top_bar_image = self.top_bar_image

        top_bar_image_webp: Union[None, Unset, str]
        if isinstance(self.top_bar_image_webp, Unset):
            top_bar_image_webp = UNSET
        else:
            top_bar_image_webp = self.top_bar_image_webp

        top_bar_vertical_image: Union[None, Unset, str]
        if isinstance(self.top_bar_vertical_image, Unset):
            top_bar_vertical_image = UNSET
        else:
            top_bar_vertical_image = self.top_bar_vertical_image

        top_bar_vertical_image_webp: Union[None, Unset, str]
        if isinstance(self.top_bar_vertical_image_webp, Unset):
            top_bar_vertical_image_webp = UNSET
        else:
            top_bar_vertical_image_webp = self.top_bar_vertical_image_webp

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

        background_image: Union[None, Unset, str]
        if isinstance(self.background_image, Unset):
            background_image = UNSET
        else:
            background_image = self.background_image

        background_image_webp: Union[None, Unset, str]
        if isinstance(self.background_image_webp, Unset):
            background_image_webp = UNSET
        else:
            background_image_webp = self.background_image_webp

        name_image: Union[None, Unset, str]
        if isinstance(self.name_image, Unset):
            name_image = UNSET
        else:
            name_image = self.name_image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if icon_hero_card is not UNSET:
            field_dict["icon_hero_card"] = icon_hero_card
        if icon_hero_card_webp is not UNSET:
            field_dict["icon_hero_card_webp"] = icon_hero_card_webp
        if icon_image_small is not UNSET:
            field_dict["icon_image_small"] = icon_image_small
        if icon_image_small_webp is not UNSET:
            field_dict["icon_image_small_webp"] = icon_image_small_webp
        if minimap_image is not UNSET:
            field_dict["minimap_image"] = minimap_image
        if minimap_image_webp is not UNSET:
            field_dict["minimap_image_webp"] = minimap_image_webp
        if selection_image is not UNSET:
            field_dict["selection_image"] = selection_image
        if selection_image_webp is not UNSET:
            field_dict["selection_image_webp"] = selection_image_webp
        if top_bar_image is not UNSET:
            field_dict["top_bar_image"] = top_bar_image
        if top_bar_image_webp is not UNSET:
            field_dict["top_bar_image_webp"] = top_bar_image_webp
        if top_bar_vertical_image is not UNSET:
            field_dict["top_bar_vertical_image"] = top_bar_vertical_image
        if top_bar_vertical_image_webp is not UNSET:
            field_dict["top_bar_vertical_image_webp"] = top_bar_vertical_image_webp
        if weapon_image is not UNSET:
            field_dict["weapon_image"] = weapon_image
        if weapon_image_webp is not UNSET:
            field_dict["weapon_image_webp"] = weapon_image_webp
        if background_image is not UNSET:
            field_dict["background_image"] = background_image
        if background_image_webp is not UNSET:
            field_dict["background_image_webp"] = background_image_webp
        if name_image is not UNSET:
            field_dict["name_image"] = name_image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_icon_hero_card(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon_hero_card = _parse_icon_hero_card(d.pop("icon_hero_card", UNSET))

        def _parse_icon_hero_card_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon_hero_card_webp = _parse_icon_hero_card_webp(d.pop("icon_hero_card_webp", UNSET))

        def _parse_icon_image_small(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon_image_small = _parse_icon_image_small(d.pop("icon_image_small", UNSET))

        def _parse_icon_image_small_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon_image_small_webp = _parse_icon_image_small_webp(d.pop("icon_image_small_webp", UNSET))

        def _parse_minimap_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        minimap_image = _parse_minimap_image(d.pop("minimap_image", UNSET))

        def _parse_minimap_image_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        minimap_image_webp = _parse_minimap_image_webp(d.pop("minimap_image_webp", UNSET))

        def _parse_selection_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        selection_image = _parse_selection_image(d.pop("selection_image", UNSET))

        def _parse_selection_image_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        selection_image_webp = _parse_selection_image_webp(d.pop("selection_image_webp", UNSET))

        def _parse_top_bar_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        top_bar_image = _parse_top_bar_image(d.pop("top_bar_image", UNSET))

        def _parse_top_bar_image_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        top_bar_image_webp = _parse_top_bar_image_webp(d.pop("top_bar_image_webp", UNSET))

        def _parse_top_bar_vertical_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        top_bar_vertical_image = _parse_top_bar_vertical_image(d.pop("top_bar_vertical_image", UNSET))

        def _parse_top_bar_vertical_image_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        top_bar_vertical_image_webp = _parse_top_bar_vertical_image_webp(d.pop("top_bar_vertical_image_webp", UNSET))

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

        def _parse_background_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        background_image = _parse_background_image(d.pop("background_image", UNSET))

        def _parse_background_image_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        background_image_webp = _parse_background_image_webp(d.pop("background_image_webp", UNSET))

        def _parse_name_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_image = _parse_name_image(d.pop("name_image", UNSET))

        hero_images_v2 = cls(
            icon_hero_card=icon_hero_card,
            icon_hero_card_webp=icon_hero_card_webp,
            icon_image_small=icon_image_small,
            icon_image_small_webp=icon_image_small_webp,
            minimap_image=minimap_image,
            minimap_image_webp=minimap_image_webp,
            selection_image=selection_image,
            selection_image_webp=selection_image_webp,
            top_bar_image=top_bar_image,
            top_bar_image_webp=top_bar_image_webp,
            top_bar_vertical_image=top_bar_vertical_image,
            top_bar_vertical_image_webp=top_bar_vertical_image_webp,
            weapon_image=weapon_image,
            weapon_image_webp=weapon_image_webp,
            background_image=background_image,
            background_image_webp=background_image_webp,
            name_image=name_image,
        )

        hero_images_v2.additional_properties = d
        return hero_images_v2

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
