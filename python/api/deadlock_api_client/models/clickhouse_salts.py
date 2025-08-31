from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClickhouseSalts")


@_attrs_define
class ClickhouseSalts:
    """
    Attributes:
        match_id (int):
        cluster_id (Union[None, Unset, int]):
        metadata_salt (Union[None, Unset, int]):
        replay_salt (Union[None, Unset, int]):
    """

    match_id: int
    cluster_id: Union[None, Unset, int] = UNSET
    metadata_salt: Union[None, Unset, int] = UNSET
    replay_salt: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match_id = self.match_id

        cluster_id: Union[None, Unset, int]
        if isinstance(self.cluster_id, Unset):
            cluster_id = UNSET
        else:
            cluster_id = self.cluster_id

        metadata_salt: Union[None, Unset, int]
        if isinstance(self.metadata_salt, Unset):
            metadata_salt = UNSET
        else:
            metadata_salt = self.metadata_salt

        replay_salt: Union[None, Unset, int]
        if isinstance(self.replay_salt, Unset):
            replay_salt = UNSET
        else:
            replay_salt = self.replay_salt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "match_id": match_id,
            }
        )
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if metadata_salt is not UNSET:
            field_dict["metadata_salt"] = metadata_salt
        if replay_salt is not UNSET:
            field_dict["replay_salt"] = replay_salt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        match_id = d.pop("match_id")

        def _parse_cluster_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cluster_id = _parse_cluster_id(d.pop("cluster_id", UNSET))

        def _parse_metadata_salt(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        metadata_salt = _parse_metadata_salt(d.pop("metadata_salt", UNSET))

        def _parse_replay_salt(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        replay_salt = _parse_replay_salt(d.pop("replay_salt", UNSET))

        clickhouse_salts = cls(
            match_id=match_id,
            cluster_id=cluster_id,
            metadata_salt=metadata_salt,
            replay_salt=replay_salt,
        )

        clickhouse_salts.additional_properties = d
        return clickhouse_salts

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
