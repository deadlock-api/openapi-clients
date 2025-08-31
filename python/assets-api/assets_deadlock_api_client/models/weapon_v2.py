from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.raw_weapon_info_v2 import RawWeaponInfoV2
    from ..models.weapon_v2_properties_type_0 import WeaponV2PropertiesType0


T = TypeVar("T", bound="WeaponV2")


@_attrs_define
class WeaponV2:
    """
    Attributes:
        id (int):
        class_name (str):
        name (str):
        start_trained (Union[None, Unset, bool]):
        image (Union[None, Unset, str]):
        image_webp (Union[None, Unset, str]):
        hero (Union[None, Unset, int]):
        heroes (Union[None, Unset, list[int]]):
        update_time (Union[None, Unset, int]):
        properties (Union['WeaponV2PropertiesType0', None, Unset]):
        weapon_info (Union['RawWeaponInfoV2', None, Unset]):
        type_ (Union[Literal['weapon'], Unset]):  Default: 'weapon'.
    """

    id: int
    class_name: str
    name: str
    start_trained: Union[None, Unset, bool] = UNSET
    image: Union[None, Unset, str] = UNSET
    image_webp: Union[None, Unset, str] = UNSET
    hero: Union[None, Unset, int] = UNSET
    heroes: Union[None, Unset, list[int]] = UNSET
    update_time: Union[None, Unset, int] = UNSET
    properties: Union["WeaponV2PropertiesType0", None, Unset] = UNSET
    weapon_info: Union["RawWeaponInfoV2", None, Unset] = UNSET
    type_: Union[Literal["weapon"], Unset] = "weapon"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.raw_weapon_info_v2 import RawWeaponInfoV2
        from ..models.weapon_v2_properties_type_0 import WeaponV2PropertiesType0

        id = self.id

        class_name = self.class_name

        name = self.name

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
        elif isinstance(self.properties, WeaponV2PropertiesType0):
            properties = self.properties.to_dict()
        else:
            properties = self.properties

        weapon_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.weapon_info, Unset):
            weapon_info = UNSET
        elif isinstance(self.weapon_info, RawWeaponInfoV2):
            weapon_info = self.weapon_info.to_dict()
        else:
            weapon_info = self.weapon_info

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "class_name": class_name,
                "name": name,
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_weapon_info_v2 import RawWeaponInfoV2
        from ..models.weapon_v2_properties_type_0 import WeaponV2PropertiesType0

        d = dict(src_dict)
        id = d.pop("id")

        class_name = d.pop("class_name")

        name = d.pop("name")

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

        def _parse_properties(data: object) -> Union["WeaponV2PropertiesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = WeaponV2PropertiesType0.from_dict(data)

                return properties_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WeaponV2PropertiesType0", None, Unset], data)

        properties = _parse_properties(d.pop("properties", UNSET))

        def _parse_weapon_info(data: object) -> Union["RawWeaponInfoV2", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                weapon_info_type_0 = RawWeaponInfoV2.from_dict(data)

                return weapon_info_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RawWeaponInfoV2", None, Unset], data)

        weapon_info = _parse_weapon_info(d.pop("weapon_info", UNSET))

        type_ = cast(Union[Literal["weapon"], Unset], d.pop("type", UNSET))
        if type_ != "weapon" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'weapon', got '{type_}'")

        weapon_v2 = cls(
            id=id,
            class_name=class_name,
            name=name,
            start_trained=start_trained,
            image=image,
            image_webp=image_webp,
            hero=hero,
            heroes=heroes,
            update_time=update_time,
            properties=properties,
            weapon_info=weapon_info,
            type_=type_,
        )

        weapon_v2.additional_properties = d
        return weapon_v2

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
