from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.build_hero_details import BuildHeroDetails


T = TypeVar("T", bound="BuildHero")


@_attrs_define
class BuildHero:
    """
    Attributes:
        author_account_id (int):
        details (BuildHeroDetails):
        hero_build_id (int):
        hero_id (int): See more: <https://assets.deadlock-api.com/v2/heroes>
        language (int):
        name (str):
        origin_build_id (int):
        version (int):
        description (Union[None, Unset, str]):
        development_build (Union[None, Unset, bool]):
        last_updated_timestamp (Union[None, Unset, int]):
        publish_timestamp (Union[None, Unset, int]):
        tags (Union[Unset, list[int]]):
    """

    author_account_id: int
    details: "BuildHeroDetails"
    hero_build_id: int
    hero_id: int
    language: int
    name: str
    origin_build_id: int
    version: int
    description: Union[None, Unset, str] = UNSET
    development_build: Union[None, Unset, bool] = UNSET
    last_updated_timestamp: Union[None, Unset, int] = UNSET
    publish_timestamp: Union[None, Unset, int] = UNSET
    tags: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_account_id = self.author_account_id

        details = self.details.to_dict()

        hero_build_id = self.hero_build_id

        hero_id = self.hero_id

        language = self.language

        name = self.name

        origin_build_id = self.origin_build_id

        version = self.version

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        development_build: Union[None, Unset, bool]
        if isinstance(self.development_build, Unset):
            development_build = UNSET
        else:
            development_build = self.development_build

        last_updated_timestamp: Union[None, Unset, int]
        if isinstance(self.last_updated_timestamp, Unset):
            last_updated_timestamp = UNSET
        else:
            last_updated_timestamp = self.last_updated_timestamp

        publish_timestamp: Union[None, Unset, int]
        if isinstance(self.publish_timestamp, Unset):
            publish_timestamp = UNSET
        else:
            publish_timestamp = self.publish_timestamp

        tags: Union[Unset, list[int]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author_account_id": author_account_id,
                "details": details,
                "hero_build_id": hero_build_id,
                "hero_id": hero_id,
                "language": language,
                "name": name,
                "origin_build_id": origin_build_id,
                "version": version,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if development_build is not UNSET:
            field_dict["development_build"] = development_build
        if last_updated_timestamp is not UNSET:
            field_dict["last_updated_timestamp"] = last_updated_timestamp
        if publish_timestamp is not UNSET:
            field_dict["publish_timestamp"] = publish_timestamp
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.build_hero_details import BuildHeroDetails

        d = dict(src_dict)
        author_account_id = d.pop("author_account_id")

        details = BuildHeroDetails.from_dict(d.pop("details"))

        hero_build_id = d.pop("hero_build_id")

        hero_id = d.pop("hero_id")

        language = d.pop("language")

        name = d.pop("name")

        origin_build_id = d.pop("origin_build_id")

        version = d.pop("version")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_development_build(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        development_build = _parse_development_build(d.pop("development_build", UNSET))

        def _parse_last_updated_timestamp(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        last_updated_timestamp = _parse_last_updated_timestamp(d.pop("last_updated_timestamp", UNSET))

        def _parse_publish_timestamp(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        publish_timestamp = _parse_publish_timestamp(d.pop("publish_timestamp", UNSET))

        tags = cast(list[int], d.pop("tags", UNSET))

        build_hero = cls(
            author_account_id=author_account_id,
            details=details,
            hero_build_id=hero_build_id,
            hero_id=hero_id,
            language=language,
            name=name,
            origin_build_id=origin_build_id,
            version=version,
            description=description,
            development_build=development_build,
            last_updated_timestamp=last_updated_timestamp,
            publish_timestamp=publish_timestamp,
            tags=tags,
        )

        build_hero.additional_properties = d
        return build_hero

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
