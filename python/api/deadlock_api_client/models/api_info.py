from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_info_table_sizes_type_0 import APIInfoTableSizesType0


T = TypeVar("T", bound="APIInfo")


@_attrs_define
class APIInfo:
    """
    Attributes:
        fetched_matches_per_day (Union[None, Unset, int]): The number of matches fetched in the last 24 hours.
        missed_matches (Union[None, Unset, int]): The number of matches that have not been fetched.
        table_sizes (Union['APIInfoTableSizesType0', None, Unset]): The sizes of all tables in the database.
    """

    fetched_matches_per_day: Union[None, Unset, int] = UNSET
    missed_matches: Union[None, Unset, int] = UNSET
    table_sizes: Union["APIInfoTableSizesType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_info_table_sizes_type_0 import APIInfoTableSizesType0

        fetched_matches_per_day: Union[None, Unset, int]
        if isinstance(self.fetched_matches_per_day, Unset):
            fetched_matches_per_day = UNSET
        else:
            fetched_matches_per_day = self.fetched_matches_per_day

        missed_matches: Union[None, Unset, int]
        if isinstance(self.missed_matches, Unset):
            missed_matches = UNSET
        else:
            missed_matches = self.missed_matches

        table_sizes: Union[None, Unset, dict[str, Any]]
        if isinstance(self.table_sizes, Unset):
            table_sizes = UNSET
        elif isinstance(self.table_sizes, APIInfoTableSizesType0):
            table_sizes = self.table_sizes.to_dict()
        else:
            table_sizes = self.table_sizes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fetched_matches_per_day is not UNSET:
            field_dict["fetched_matches_per_day"] = fetched_matches_per_day
        if missed_matches is not UNSET:
            field_dict["missed_matches"] = missed_matches
        if table_sizes is not UNSET:
            field_dict["table_sizes"] = table_sizes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_info_table_sizes_type_0 import APIInfoTableSizesType0

        d = dict(src_dict)

        def _parse_fetched_matches_per_day(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fetched_matches_per_day = _parse_fetched_matches_per_day(d.pop("fetched_matches_per_day", UNSET))

        def _parse_missed_matches(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        missed_matches = _parse_missed_matches(d.pop("missed_matches", UNSET))

        def _parse_table_sizes(data: object) -> Union["APIInfoTableSizesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                table_sizes_type_0 = APIInfoTableSizesType0.from_dict(data)

                return table_sizes_type_0
            except:  # noqa: E722
                pass
            return cast(Union["APIInfoTableSizesType0", None, Unset], data)

        table_sizes = _parse_table_sizes(d.pop("table_sizes", UNSET))

        api_info = cls(
            fetched_matches_per_day=fetched_matches_per_day,
            missed_matches=missed_matches,
            table_sizes=table_sizes,
        )

        api_info.additional_properties = d
        return api_info

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
