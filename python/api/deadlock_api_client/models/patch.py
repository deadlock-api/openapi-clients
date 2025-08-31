import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.patch_category import PatchCategory
    from ..models.patch_guid import PatchGuid


T = TypeVar("T", bound="Patch")


@_attrs_define
class Patch:
    """
    Attributes:
        author (str):
        category (PatchCategory):
        content_encoded (str):
        dc_creator (str):
        guid (PatchGuid):
        link (str):
        pub_date (datetime.datetime):
        slash_comments (str):
        title (str):
    """

    author: str
    category: "PatchCategory"
    content_encoded: str
    dc_creator: str
    guid: "PatchGuid"
    link: str
    pub_date: datetime.datetime
    slash_comments: str
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author

        category = self.category.to_dict()

        content_encoded = self.content_encoded

        dc_creator = self.dc_creator

        guid = self.guid.to_dict()

        link = self.link

        pub_date = self.pub_date.isoformat()

        slash_comments = self.slash_comments

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author": author,
                "category": category,
                "content_encoded": content_encoded,
                "dc_creator": dc_creator,
                "guid": guid,
                "link": link,
                "pub_date": pub_date,
                "slash_comments": slash_comments,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_category import PatchCategory
        from ..models.patch_guid import PatchGuid

        d = dict(src_dict)
        author = d.pop("author")

        category = PatchCategory.from_dict(d.pop("category"))

        content_encoded = d.pop("content_encoded")

        dc_creator = d.pop("dc_creator")

        guid = PatchGuid.from_dict(d.pop("guid"))

        link = d.pop("link")

        pub_date = isoparse(d.pop("pub_date"))

        slash_comments = d.pop("slash_comments")

        title = d.pop("title")

        patch = cls(
            author=author,
            category=category,
            content_encoded=content_encoded,
            dc_creator=dc_creator,
            guid=guid,
            link=link,
            pub_date=pub_date,
            slash_comments=slash_comments,
            title=title,
        )

        patch.additional_properties = d
        return patch

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
