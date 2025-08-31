from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCustomResponse")


@_attrs_define
class CreateCustomResponse:
    """
    Attributes:
        party_code (str):
        party_id (str):
        callback_secret (Union[None, Unset, str]): If a callback url is provided, this is the secret that should be used
            to verify the callback.
            The secret is a base64 encoded random string. To verify it you should compare it with the X-Callback-Secret
            header.
            If no callback url is provided, this will be None.
    """

    party_code: str
    party_id: str
    callback_secret: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        party_code = self.party_code

        party_id = self.party_id

        callback_secret: Union[None, Unset, str]
        if isinstance(self.callback_secret, Unset):
            callback_secret = UNSET
        else:
            callback_secret = self.callback_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "party_code": party_code,
                "party_id": party_id,
            }
        )
        if callback_secret is not UNSET:
            field_dict["callback_secret"] = callback_secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        party_code = d.pop("party_code")

        party_id = d.pop("party_id")

        def _parse_callback_secret(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        callback_secret = _parse_callback_secret(d.pop("callback_secret", UNSET))

        create_custom_response = cls(
            party_code=party_code,
            party_id=party_id,
            callback_secret=callback_secret,
        )

        create_custom_response.additional_properties = d
        return create_custom_response

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
