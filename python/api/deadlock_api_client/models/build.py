from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.build_hero import BuildHero


T = TypeVar("T", bound="Build")


@_attrs_define
class Build:
    """
    Attributes:
        hero_build (BuildHero):
        num_favorites (Union[None, Unset, int]):
        num_ignores (Union[None, Unset, int]):
        num_reports (Union[None, Unset, int]):
        num_weekly_favorites (Union[None, Unset, int]):
        rollup_category (Union[None, Unset, int]):
    """

    hero_build: "BuildHero"
    num_favorites: Union[None, Unset, int] = UNSET
    num_ignores: Union[None, Unset, int] = UNSET
    num_reports: Union[None, Unset, int] = UNSET
    num_weekly_favorites: Union[None, Unset, int] = UNSET
    rollup_category: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hero_build = self.hero_build.to_dict()

        num_favorites: Union[None, Unset, int]
        if isinstance(self.num_favorites, Unset):
            num_favorites = UNSET
        else:
            num_favorites = self.num_favorites

        num_ignores: Union[None, Unset, int]
        if isinstance(self.num_ignores, Unset):
            num_ignores = UNSET
        else:
            num_ignores = self.num_ignores

        num_reports: Union[None, Unset, int]
        if isinstance(self.num_reports, Unset):
            num_reports = UNSET
        else:
            num_reports = self.num_reports

        num_weekly_favorites: Union[None, Unset, int]
        if isinstance(self.num_weekly_favorites, Unset):
            num_weekly_favorites = UNSET
        else:
            num_weekly_favorites = self.num_weekly_favorites

        rollup_category: Union[None, Unset, int]
        if isinstance(self.rollup_category, Unset):
            rollup_category = UNSET
        else:
            rollup_category = self.rollup_category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hero_build": hero_build,
            }
        )
        if num_favorites is not UNSET:
            field_dict["num_favorites"] = num_favorites
        if num_ignores is not UNSET:
            field_dict["num_ignores"] = num_ignores
        if num_reports is not UNSET:
            field_dict["num_reports"] = num_reports
        if num_weekly_favorites is not UNSET:
            field_dict["num_weekly_favorites"] = num_weekly_favorites
        if rollup_category is not UNSET:
            field_dict["rollup_category"] = rollup_category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.build_hero import BuildHero

        d = dict(src_dict)
        hero_build = BuildHero.from_dict(d.pop("hero_build"))

        def _parse_num_favorites(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        num_favorites = _parse_num_favorites(d.pop("num_favorites", UNSET))

        def _parse_num_ignores(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        num_ignores = _parse_num_ignores(d.pop("num_ignores", UNSET))

        def _parse_num_reports(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        num_reports = _parse_num_reports(d.pop("num_reports", UNSET))

        def _parse_num_weekly_favorites(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        num_weekly_favorites = _parse_num_weekly_favorites(d.pop("num_weekly_favorites", UNSET))

        def _parse_rollup_category(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rollup_category = _parse_rollup_category(d.pop("rollup_category", UNSET))

        build = cls(
            hero_build=hero_build,
            num_favorites=num_favorites,
            num_ignores=num_ignores,
            num_reports=num_reports,
            num_weekly_favorites=num_weekly_favorites,
            rollup_category=rollup_category,
        )

        build.additional_properties = d
        return build

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
