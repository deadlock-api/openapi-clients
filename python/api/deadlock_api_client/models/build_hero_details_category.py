from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.build_hero_details_category_ability import BuildHeroDetailsCategoryAbility


T = TypeVar("T", bound="BuildHeroDetailsCategory")


@_attrs_define
class BuildHeroDetailsCategory:
    """
    Attributes:
        name (str):
        description (Union[None, Unset, str]):
        height (Union[None, Unset, float]):
        mods (Union[None, Unset, list['BuildHeroDetailsCategoryAbility']]):
        optional (Union[None, Unset, bool]):
        width (Union[None, Unset, float]):
    """

    name: str
    description: Union[None, Unset, str] = UNSET
    height: Union[None, Unset, float] = UNSET
    mods: Union[None, Unset, list["BuildHeroDetailsCategoryAbility"]] = UNSET
    optional: Union[None, Unset, bool] = UNSET
    width: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        height: Union[None, Unset, float]
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        mods: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.mods, Unset):
            mods = UNSET
        elif isinstance(self.mods, list):
            mods = []
            for mods_type_0_item_data in self.mods:
                mods_type_0_item = mods_type_0_item_data.to_dict()
                mods.append(mods_type_0_item)

        else:
            mods = self.mods

        optional: Union[None, Unset, bool]
        if isinstance(self.optional, Unset):
            optional = UNSET
        else:
            optional = self.optional

        width: Union[None, Unset, float]
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if height is not UNSET:
            field_dict["height"] = height
        if mods is not UNSET:
            field_dict["mods"] = mods
        if optional is not UNSET:
            field_dict["optional"] = optional
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.build_hero_details_category_ability import BuildHeroDetailsCategoryAbility

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_height(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        height = _parse_height(d.pop("height", UNSET))

        def _parse_mods(data: object) -> Union[None, Unset, list["BuildHeroDetailsCategoryAbility"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mods_type_0 = []
                _mods_type_0 = data
                for mods_type_0_item_data in _mods_type_0:
                    mods_type_0_item = BuildHeroDetailsCategoryAbility.from_dict(mods_type_0_item_data)

                    mods_type_0.append(mods_type_0_item)

                return mods_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["BuildHeroDetailsCategoryAbility"]], data)

        mods = _parse_mods(d.pop("mods", UNSET))

        def _parse_optional(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        optional = _parse_optional(d.pop("optional", UNSET))

        def _parse_width(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        width = _parse_width(d.pop("width", UNSET))

        build_hero_details_category = cls(
            name=name,
            description=description,
            height=height,
            mods=mods,
            optional=optional,
            width=width,
        )

        build_hero_details_category.additional_properties = d
        return build_hero_details_category

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
