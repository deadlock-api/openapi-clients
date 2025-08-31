from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_slot_type_v2 import ItemSlotTypeV2
from ..models.item_tier_v2 import ItemTierV2
from ..models.raw_ability_activation_v2 import RawAbilityActivationV2
from ..models.raw_ability_imbue_v2 import RawAbilityImbueV2
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.raw_item_weapon_info_v2 import RawItemWeaponInfoV2
    from ..models.upgrade_description_v2 import UpgradeDescriptionV2
    from ..models.upgrade_tooltip_section_v2 import UpgradeTooltipSectionV2
    from ..models.upgrade_v2_properties_type_0 import UpgradeV2PropertiesType0


T = TypeVar("T", bound="UpgradeV2")


@_attrs_define
class UpgradeV2:
    """
    Attributes:
        id (int):
        class_name (str):
        name (str):
        item_slot_type (ItemSlotTypeV2):
        item_tier (ItemTierV2):
        activation (RawAbilityActivationV2):
        is_active_item (bool):
        shopable (bool):
        cost (Union[None, int]):
        start_trained (Union[None, Unset, bool]):
        image (Union[None, Unset, str]):
        image_webp (Union[None, Unset, str]):
        hero (Union[None, Unset, int]):
        heroes (Union[None, Unset, list[int]]):
        update_time (Union[None, Unset, int]):
        properties (Union['UpgradeV2PropertiesType0', None, Unset]):
        weapon_info (Union['RawItemWeaponInfoV2', None, Unset]):
        type_ (Union[Literal['upgrade'], Unset]):  Default: 'upgrade'.
        shop_image (Union[None, Unset, str]):
        shop_image_webp (Union[None, Unset, str]):
        shop_image_small (Union[None, Unset, str]):
        shop_image_small_webp (Union[None, Unset, str]):
        disabled (Union[None, Unset, bool]):
        description (Union['UpgradeDescriptionV2', None, Unset]):
        imbue (Union[None, RawAbilityImbueV2, Unset]):
        component_items (Union[None, Unset, list[str]]):
        tooltip_sections (Union[None, Unset, list['UpgradeTooltipSectionV2']]):
    """

    id: int
    class_name: str
    name: str
    item_slot_type: ItemSlotTypeV2
    item_tier: ItemTierV2
    activation: RawAbilityActivationV2
    is_active_item: bool
    shopable: bool
    cost: Union[None, int]
    start_trained: Union[None, Unset, bool] = UNSET
    image: Union[None, Unset, str] = UNSET
    image_webp: Union[None, Unset, str] = UNSET
    hero: Union[None, Unset, int] = UNSET
    heroes: Union[None, Unset, list[int]] = UNSET
    update_time: Union[None, Unset, int] = UNSET
    properties: Union["UpgradeV2PropertiesType0", None, Unset] = UNSET
    weapon_info: Union["RawItemWeaponInfoV2", None, Unset] = UNSET
    type_: Union[Literal["upgrade"], Unset] = "upgrade"
    shop_image: Union[None, Unset, str] = UNSET
    shop_image_webp: Union[None, Unset, str] = UNSET
    shop_image_small: Union[None, Unset, str] = UNSET
    shop_image_small_webp: Union[None, Unset, str] = UNSET
    disabled: Union[None, Unset, bool] = UNSET
    description: Union["UpgradeDescriptionV2", None, Unset] = UNSET
    imbue: Union[None, RawAbilityImbueV2, Unset] = UNSET
    component_items: Union[None, Unset, list[str]] = UNSET
    tooltip_sections: Union[None, Unset, list["UpgradeTooltipSectionV2"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.raw_item_weapon_info_v2 import RawItemWeaponInfoV2
        from ..models.upgrade_description_v2 import UpgradeDescriptionV2
        from ..models.upgrade_v2_properties_type_0 import UpgradeV2PropertiesType0

        id = self.id

        class_name = self.class_name

        name = self.name

        item_slot_type = self.item_slot_type.value

        item_tier = self.item_tier.value

        activation = self.activation.value

        is_active_item = self.is_active_item

        shopable = self.shopable

        cost: Union[None, int]
        cost = self.cost

        start_trained: Union[None, Unset, bool]
        if isinstance(self.start_trained, Unset):
            start_trained = UNSET
        else:
            start_trained = self.start_trained

        image: Union[None, Unset, str]
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        image_webp: Union[None, Unset, str]
        if isinstance(self.image_webp, Unset):
            image_webp = UNSET
        else:
            image_webp = self.image_webp

        hero: Union[None, Unset, int]
        if isinstance(self.hero, Unset):
            hero = UNSET
        else:
            hero = self.hero

        heroes: Union[None, Unset, list[int]]
        if isinstance(self.heroes, Unset):
            heroes = UNSET
        elif isinstance(self.heroes, list):
            heroes = self.heroes

        else:
            heroes = self.heroes

        update_time: Union[None, Unset, int]
        if isinstance(self.update_time, Unset):
            update_time = UNSET
        else:
            update_time = self.update_time

        properties: Union[None, Unset, dict[str, Any]]
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif isinstance(self.properties, UpgradeV2PropertiesType0):
            properties = self.properties.to_dict()
        else:
            properties = self.properties

        weapon_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.weapon_info, Unset):
            weapon_info = UNSET
        elif isinstance(self.weapon_info, RawItemWeaponInfoV2):
            weapon_info = self.weapon_info.to_dict()
        else:
            weapon_info = self.weapon_info

        type_ = self.type_

        shop_image: Union[None, Unset, str]
        if isinstance(self.shop_image, Unset):
            shop_image = UNSET
        else:
            shop_image = self.shop_image

        shop_image_webp: Union[None, Unset, str]
        if isinstance(self.shop_image_webp, Unset):
            shop_image_webp = UNSET
        else:
            shop_image_webp = self.shop_image_webp

        shop_image_small: Union[None, Unset, str]
        if isinstance(self.shop_image_small, Unset):
            shop_image_small = UNSET
        else:
            shop_image_small = self.shop_image_small

        shop_image_small_webp: Union[None, Unset, str]
        if isinstance(self.shop_image_small_webp, Unset):
            shop_image_small_webp = UNSET
        else:
            shop_image_small_webp = self.shop_image_small_webp

        disabled: Union[None, Unset, bool]
        if isinstance(self.disabled, Unset):
            disabled = UNSET
        else:
            disabled = self.disabled

        description: Union[None, Unset, dict[str, Any]]
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, UpgradeDescriptionV2):
            description = self.description.to_dict()
        else:
            description = self.description

        imbue: Union[None, Unset, str]
        if isinstance(self.imbue, Unset):
            imbue = UNSET
        elif isinstance(self.imbue, RawAbilityImbueV2):
            imbue = self.imbue.value
        else:
            imbue = self.imbue

        component_items: Union[None, Unset, list[str]]
        if isinstance(self.component_items, Unset):
            component_items = UNSET
        elif isinstance(self.component_items, list):
            component_items = self.component_items

        else:
            component_items = self.component_items

        tooltip_sections: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.tooltip_sections, Unset):
            tooltip_sections = UNSET
        elif isinstance(self.tooltip_sections, list):
            tooltip_sections = []
            for tooltip_sections_type_0_item_data in self.tooltip_sections:
                tooltip_sections_type_0_item = tooltip_sections_type_0_item_data.to_dict()
                tooltip_sections.append(tooltip_sections_type_0_item)

        else:
            tooltip_sections = self.tooltip_sections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "class_name": class_name,
                "name": name,
                "item_slot_type": item_slot_type,
                "item_tier": item_tier,
                "activation": activation,
                "is_active_item": is_active_item,
                "shopable": shopable,
                "cost": cost,
            }
        )
        if start_trained is not UNSET:
            field_dict["start_trained"] = start_trained
        if image is not UNSET:
            field_dict["image"] = image
        if image_webp is not UNSET:
            field_dict["image_webp"] = image_webp
        if hero is not UNSET:
            field_dict["hero"] = hero
        if heroes is not UNSET:
            field_dict["heroes"] = heroes
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if properties is not UNSET:
            field_dict["properties"] = properties
        if weapon_info is not UNSET:
            field_dict["weapon_info"] = weapon_info
        if type_ is not UNSET:
            field_dict["type"] = type_
        if shop_image is not UNSET:
            field_dict["shop_image"] = shop_image
        if shop_image_webp is not UNSET:
            field_dict["shop_image_webp"] = shop_image_webp
        if shop_image_small is not UNSET:
            field_dict["shop_image_small"] = shop_image_small
        if shop_image_small_webp is not UNSET:
            field_dict["shop_image_small_webp"] = shop_image_small_webp
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if description is not UNSET:
            field_dict["description"] = description
        if imbue is not UNSET:
            field_dict["imbue"] = imbue
        if component_items is not UNSET:
            field_dict["component_items"] = component_items
        if tooltip_sections is not UNSET:
            field_dict["tooltip_sections"] = tooltip_sections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_item_weapon_info_v2 import RawItemWeaponInfoV2
        from ..models.upgrade_description_v2 import UpgradeDescriptionV2
        from ..models.upgrade_tooltip_section_v2 import UpgradeTooltipSectionV2
        from ..models.upgrade_v2_properties_type_0 import UpgradeV2PropertiesType0

        d = dict(src_dict)
        id = d.pop("id")

        class_name = d.pop("class_name")

        name = d.pop("name")

        item_slot_type = ItemSlotTypeV2(d.pop("item_slot_type"))

        item_tier = ItemTierV2(d.pop("item_tier"))

        activation = RawAbilityActivationV2(d.pop("activation"))

        is_active_item = d.pop("is_active_item")

        shopable = d.pop("shopable")

        def _parse_cost(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        cost = _parse_cost(d.pop("cost"))

        def _parse_start_trained(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        start_trained = _parse_start_trained(d.pop("start_trained", UNSET))

        def _parse_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_image_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image_webp = _parse_image_webp(d.pop("image_webp", UNSET))

        def _parse_hero(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        hero = _parse_hero(d.pop("hero", UNSET))

        def _parse_heroes(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                heroes_type_0 = cast(list[int], data)

                return heroes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        heroes = _parse_heroes(d.pop("heroes", UNSET))

        def _parse_update_time(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        update_time = _parse_update_time(d.pop("update_time", UNSET))

        def _parse_properties(data: object) -> Union["UpgradeV2PropertiesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = UpgradeV2PropertiesType0.from_dict(data)

                return properties_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpgradeV2PropertiesType0", None, Unset], data)

        properties = _parse_properties(d.pop("properties", UNSET))

        def _parse_weapon_info(data: object) -> Union["RawItemWeaponInfoV2", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                weapon_info_type_0 = RawItemWeaponInfoV2.from_dict(data)

                return weapon_info_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RawItemWeaponInfoV2", None, Unset], data)

        weapon_info = _parse_weapon_info(d.pop("weapon_info", UNSET))

        type_ = cast(Union[Literal["upgrade"], Unset], d.pop("type", UNSET))
        if type_ != "upgrade" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'upgrade', got '{type_}'")

        def _parse_shop_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shop_image = _parse_shop_image(d.pop("shop_image", UNSET))

        def _parse_shop_image_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shop_image_webp = _parse_shop_image_webp(d.pop("shop_image_webp", UNSET))

        def _parse_shop_image_small(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shop_image_small = _parse_shop_image_small(d.pop("shop_image_small", UNSET))

        def _parse_shop_image_small_webp(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shop_image_small_webp = _parse_shop_image_small_webp(d.pop("shop_image_small_webp", UNSET))

        def _parse_disabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        disabled = _parse_disabled(d.pop("disabled", UNSET))

        def _parse_description(data: object) -> Union["UpgradeDescriptionV2", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                description_type_0 = UpgradeDescriptionV2.from_dict(data)

                return description_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpgradeDescriptionV2", None, Unset], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_imbue(data: object) -> Union[None, RawAbilityImbueV2, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                imbue_type_0 = RawAbilityImbueV2(data)

                return imbue_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, RawAbilityImbueV2, Unset], data)

        imbue = _parse_imbue(d.pop("imbue", UNSET))

        def _parse_component_items(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                component_items_type_0 = cast(list[str], data)

                return component_items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        component_items = _parse_component_items(d.pop("component_items", UNSET))

        def _parse_tooltip_sections(data: object) -> Union[None, Unset, list["UpgradeTooltipSectionV2"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tooltip_sections_type_0 = []
                _tooltip_sections_type_0 = data
                for tooltip_sections_type_0_item_data in _tooltip_sections_type_0:
                    tooltip_sections_type_0_item = UpgradeTooltipSectionV2.from_dict(tooltip_sections_type_0_item_data)

                    tooltip_sections_type_0.append(tooltip_sections_type_0_item)

                return tooltip_sections_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["UpgradeTooltipSectionV2"]], data)

        tooltip_sections = _parse_tooltip_sections(d.pop("tooltip_sections", UNSET))

        upgrade_v2 = cls(
            id=id,
            class_name=class_name,
            name=name,
            item_slot_type=item_slot_type,
            item_tier=item_tier,
            activation=activation,
            is_active_item=is_active_item,
            shopable=shopable,
            cost=cost,
            start_trained=start_trained,
            image=image,
            image_webp=image_webp,
            hero=hero,
            heroes=heroes,
            update_time=update_time,
            properties=properties,
            weapon_info=weapon_info,
            type_=type_,
            shop_image=shop_image,
            shop_image_webp=shop_image_webp,
            shop_image_small=shop_image_small,
            shop_image_small_webp=shop_image_small_webp,
            disabled=disabled,
            description=description,
            imbue=imbue,
            component_items=component_items,
            tooltip_sections=tooltip_sections,
        )

        upgrade_v2.additional_properties = d
        return upgrade_v2

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
