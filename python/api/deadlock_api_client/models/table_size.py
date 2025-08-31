from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TableSize")


@_attrs_define
class TableSize:
    """
    Attributes:
        is_view (bool): Whether the table is a view.
        data_compressed_bytes (Union[None, Unset, int]): Compressed size of the table in bytes.
        data_uncompressed_bytes (Union[None, Unset, int]): Uncompressed size of the table in bytes.
        rows (Union[None, Unset, int]): Number of rows in the table.
    """

    is_view: bool
    data_compressed_bytes: Union[None, Unset, int] = UNSET
    data_uncompressed_bytes: Union[None, Unset, int] = UNSET
    rows: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_view = self.is_view

        data_compressed_bytes: Union[None, Unset, int]
        if isinstance(self.data_compressed_bytes, Unset):
            data_compressed_bytes = UNSET
        else:
            data_compressed_bytes = self.data_compressed_bytes

        data_uncompressed_bytes: Union[None, Unset, int]
        if isinstance(self.data_uncompressed_bytes, Unset):
            data_uncompressed_bytes = UNSET
        else:
            data_uncompressed_bytes = self.data_uncompressed_bytes

        rows: Union[None, Unset, int]
        if isinstance(self.rows, Unset):
            rows = UNSET
        else:
            rows = self.rows

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_view": is_view,
            }
        )
        if data_compressed_bytes is not UNSET:
            field_dict["data_compressed_bytes"] = data_compressed_bytes
        if data_uncompressed_bytes is not UNSET:
            field_dict["data_uncompressed_bytes"] = data_uncompressed_bytes
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_view = d.pop("is_view")

        def _parse_data_compressed_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        data_compressed_bytes = _parse_data_compressed_bytes(d.pop("data_compressed_bytes", UNSET))

        def _parse_data_uncompressed_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        data_uncompressed_bytes = _parse_data_uncompressed_bytes(d.pop("data_uncompressed_bytes", UNSET))

        def _parse_rows(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rows = _parse_rows(d.pop("rows", UNSET))

        table_size = cls(
            is_view=is_view,
            data_compressed_bytes=data_compressed_bytes,
            data_uncompressed_bytes=data_uncompressed_bytes,
            rows=rows,
        )

        table_size.additional_properties = d
        return table_size

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
