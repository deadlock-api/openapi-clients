import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SteamProfile")


@_attrs_define
class SteamProfile:
    """
    Attributes:
        account_id (int):
        avatar (str):
        avatarfull (str):
        avatarmedium (str):
        last_updated (datetime.datetime):
        personaname (str):
        profileurl (str):
        countrycode (Union[None, Unset, str]):
        realname (Union[None, Unset, str]):
    """

    account_id: int
    avatar: str
    avatarfull: str
    avatarmedium: str
    last_updated: datetime.datetime
    personaname: str
    profileurl: str
    countrycode: Union[None, Unset, str] = UNSET
    realname: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        avatar = self.avatar

        avatarfull = self.avatarfull

        avatarmedium = self.avatarmedium

        last_updated = self.last_updated.isoformat()

        personaname = self.personaname

        profileurl = self.profileurl

        countrycode: Union[None, Unset, str]
        if isinstance(self.countrycode, Unset):
            countrycode = UNSET
        else:
            countrycode = self.countrycode

        realname: Union[None, Unset, str]
        if isinstance(self.realname, Unset):
            realname = UNSET
        else:
            realname = self.realname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "avatar": avatar,
                "avatarfull": avatarfull,
                "avatarmedium": avatarmedium,
                "last_updated": last_updated,
                "personaname": personaname,
                "profileurl": profileurl,
            }
        )
        if countrycode is not UNSET:
            field_dict["countrycode"] = countrycode
        if realname is not UNSET:
            field_dict["realname"] = realname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        avatar = d.pop("avatar")

        avatarfull = d.pop("avatarfull")

        avatarmedium = d.pop("avatarmedium")

        last_updated = isoparse(d.pop("last_updated"))

        personaname = d.pop("personaname")

        profileurl = d.pop("profileurl")

        def _parse_countrycode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        countrycode = _parse_countrycode(d.pop("countrycode", UNSET))

        def _parse_realname(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        realname = _parse_realname(d.pop("realname", UNSET))

        steam_profile = cls(
            account_id=account_id,
            avatar=avatar,
            avatarfull=avatarfull,
            avatarmedium=avatarmedium,
            last_updated=last_updated,
            personaname=personaname,
            profileurl=profileurl,
            countrycode=countrycode,
            realname=realname,
        )

        steam_profile.additional_properties = d
        return steam_profile

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
