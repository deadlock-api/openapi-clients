from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ability_type_v2 import AbilityTypeV2
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ability_description_v2 import AbilityDescriptionV2
    from ..models.ability_tooltip_details_v2 import AbilityTooltipDetailsV2
    from ..models.ability_v2_properties_type_0 import AbilityV2PropertiesType0
    from ..models.ability_videos_v2 import AbilityVideosV2
    from ..models.raw_ability_upgrade_v2 import RawAbilityUpgradeV2
    from ..models.raw_item_weapon_info_v2 import RawItemWeaponInfoV2


T = TypeVar("T", bound="AbilityV2")


@_attrs_define
class AbilityV2:
    """
    Attributes:
        id (int):
        class_name (str):
        name (str):
        description (AbilityDescriptionV2):
        start_trained (Union[None, Unset, bool]):
        image (Union[None, Unset, str]):
        image_webp (Union[None, Unset, str]):
        hero (Union[None, Unset, int]):
        heroes (Union[None, Unset, list[int]]):
        update_time (Union[None, Unset, int]):
        properties (Union['AbilityV2PropertiesType0', None, Unset]):
        weapon_info (Union['RawItemWeaponInfoV2', None, Unset]):
        type_ (Union[Literal['ability'], Unset]):  Default: 'ability'.
        behaviours (Union[None, Unset, list[str]]):
        tooltip_details (Union['AbilityTooltipDetailsV2', None, Unset]):
        upgrades (Union[None, Unset, list['RawAbilityUpgradeV2']]):
        ability_type (Union[AbilityTypeV2, None, Unset]):
        boss_damage_scale (Union[None, Unset, float]):
        dependant_abilities (Union[None, Unset, list[str]]):
        videos (Union['AbilityVideosV2', None, Unset]):
    """

    id: int
    class_name: str
    name: str
    description: "AbilityDescriptionV2"
    start_trained: Union[None, Unset, bool] = UNSET
    image: Union[None, Unset, str] = UNSET
    image_webp: Union[None, Unset, str] = UNSET
    hero: Union[None, Unset, int] = UNSET
    heroes: Union[None, Unset, list[int]] = UNSET
    update_time: Union[None, Unset, int] = UNSET
    properties: Union["AbilityV2PropertiesType0", None, Unset] = UNSET
    weapon_info: Union["RawItemWeaponInfoV2", None, Unset] = UNSET
    type_: Union[Literal["ability"], Unset] = "ability"
    behaviours: Union[None, Unset, list[str]] = UNSET
    tooltip_details: Union["AbilityTooltipDetailsV2", None, Unset] = UNSET
    upgrades: Union[None, Unset, list["RawAbilityUpgradeV2"]] = UNSET
    ability_type: Union[AbilityTypeV2, None, Unset] = UNSET
    boss_damage_scale: Union[None, Unset, float] = UNSET
    dependant_abilities: Union[None, Unset, list[str]] = UNSET
    videos: Union["AbilityVideosV2", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ability_tooltip_details_v2 import AbilityTooltipDetailsV2
        from ..models.ability_v2_properties_type_0 import AbilityV2PropertiesType0
        from ..models.ability_videos_v2 import AbilityVideosV2
        from ..models.raw_item_weapon_info_v2 import RawItemWeaponInfoV2

        id = self.id

        class_name = self.class_name

        name = self.name

        description = self.description.to_dict()

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
        elif isinstance(self.properties, AbilityV2PropertiesType0):
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

        behaviours: Union[None, Unset, list[str]]
        if isinstance(self.behaviours, Unset):
            behaviours = UNSET
        elif isinstance(self.behaviours, list):
            behaviours = self.behaviours

        else:
            behaviours = self.behaviours

        tooltip_details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tooltip_details, Unset):
            tooltip_details = UNSET
        elif isinstance(self.tooltip_details, AbilityTooltipDetailsV2):
            tooltip_details = self.tooltip_details.to_dict()
        else:
            tooltip_details = self.tooltip_details

        upgrades: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.upgrades, Unset):
            upgrades = UNSET
        elif isinstance(self.upgrades, list):
            upgrades = []
            for upgrades_type_0_item_data in self.upgrades:
                upgrades_type_0_item = upgrades_type_0_item_data.to_dict()
                upgrades.append(upgrades_type_0_item)

        else:
            upgrades = self.upgrades

        ability_type: Union[None, Unset, str]
        if isinstance(self.ability_type, Unset):
            ability_type = UNSET
        elif isinstance(self.ability_type, AbilityTypeV2):
            ability_type = self.ability_type.value
        else:
            ability_type = self.ability_type

        boss_damage_scale: Union[None, Unset, float]
        if isinstance(self.boss_damage_scale, Unset):
            boss_damage_scale = UNSET
        else:
            boss_damage_scale = self.boss_damage_scale

        dependant_abilities: Union[None, Unset, list[str]]
        if isinstance(self.dependant_abilities, Unset):
            dependant_abilities = UNSET
        elif isinstance(self.dependant_abilities, list):
            dependant_abilities = self.dependant_abilities

        else:
            dependant_abilities = self.dependant_abilities

        videos: Union[None, Unset, dict[str, Any]]
        if isinstance(self.videos, Unset):
            videos = UNSET
        elif isinstance(self.videos, AbilityVideosV2):
            videos = self.videos.to_dict()
        else:
            videos = self.videos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "class_name": class_name,
                "name": name,
                "description": description,
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
        if behaviours is not UNSET:
            field_dict["behaviours"] = behaviours
        if tooltip_details is not UNSET:
            field_dict["tooltip_details"] = tooltip_details
        if upgrades is not UNSET:
            field_dict["upgrades"] = upgrades
        if ability_type is not UNSET:
            field_dict["ability_type"] = ability_type
        if boss_damage_scale is not UNSET:
            field_dict["boss_damage_scale"] = boss_damage_scale
        if dependant_abilities is not UNSET:
            field_dict["dependant_abilities"] = dependant_abilities
        if videos is not UNSET:
            field_dict["videos"] = videos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ability_description_v2 import AbilityDescriptionV2
        from ..models.ability_tooltip_details_v2 import AbilityTooltipDetailsV2
        from ..models.ability_v2_properties_type_0 import AbilityV2PropertiesType0
        from ..models.ability_videos_v2 import AbilityVideosV2
        from ..models.raw_ability_upgrade_v2 import RawAbilityUpgradeV2
        from ..models.raw_item_weapon_info_v2 import RawItemWeaponInfoV2

        d = dict(src_dict)
        id = d.pop("id")

        class_name = d.pop("class_name")

        name = d.pop("name")

        description = AbilityDescriptionV2.from_dict(d.pop("description"))

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

        def _parse_properties(data: object) -> Union["AbilityV2PropertiesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = AbilityV2PropertiesType0.from_dict(data)

                return properties_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AbilityV2PropertiesType0", None, Unset], data)

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

        type_ = cast(Union[Literal["ability"], Unset], d.pop("type", UNSET))
        if type_ != "ability" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'ability', got '{type_}'")

        def _parse_behaviours(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                behaviours_type_0 = cast(list[str], data)

                return behaviours_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        behaviours = _parse_behaviours(d.pop("behaviours", UNSET))

        def _parse_tooltip_details(data: object) -> Union["AbilityTooltipDetailsV2", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tooltip_details_type_0 = AbilityTooltipDetailsV2.from_dict(data)

                return tooltip_details_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AbilityTooltipDetailsV2", None, Unset], data)

        tooltip_details = _parse_tooltip_details(d.pop("tooltip_details", UNSET))

        def _parse_upgrades(data: object) -> Union[None, Unset, list["RawAbilityUpgradeV2"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                upgrades_type_0 = []
                _upgrades_type_0 = data
                for upgrades_type_0_item_data in _upgrades_type_0:
                    upgrades_type_0_item = RawAbilityUpgradeV2.from_dict(upgrades_type_0_item_data)

                    upgrades_type_0.append(upgrades_type_0_item)

                return upgrades_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["RawAbilityUpgradeV2"]], data)

        upgrades = _parse_upgrades(d.pop("upgrades", UNSET))

        def _parse_ability_type(data: object) -> Union[AbilityTypeV2, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ability_type_type_0 = AbilityTypeV2(data)

                return ability_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[AbilityTypeV2, None, Unset], data)

        ability_type = _parse_ability_type(d.pop("ability_type", UNSET))

        def _parse_boss_damage_scale(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        boss_damage_scale = _parse_boss_damage_scale(d.pop("boss_damage_scale", UNSET))

        def _parse_dependant_abilities(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dependant_abilities_type_0 = cast(list[str], data)

                return dependant_abilities_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        dependant_abilities = _parse_dependant_abilities(d.pop("dependant_abilities", UNSET))

        def _parse_videos(data: object) -> Union["AbilityVideosV2", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                videos_type_0 = AbilityVideosV2.from_dict(data)

                return videos_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AbilityVideosV2", None, Unset], data)

        videos = _parse_videos(d.pop("videos", UNSET))

        ability_v2 = cls(
            id=id,
            class_name=class_name,
            name=name,
            description=description,
            start_trained=start_trained,
            image=image,
            image_webp=image_webp,
            hero=hero,
            heroes=heroes,
            update_time=update_time,
            properties=properties,
            weapon_info=weapon_info,
            type_=type_,
            behaviours=behaviours,
            tooltip_details=tooltip_details,
            upgrades=upgrades,
            ability_type=ability_type,
            boss_damage_scale=boss_damage_scale,
            dependant_abilities=dependant_abilities,
            videos=videos,
        )

        ability_v2.additional_properties = d
        return ability_v2

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
