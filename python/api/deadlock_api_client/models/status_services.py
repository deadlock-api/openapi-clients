from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatusServices")


@_attrs_define
class StatusServices:
    """
    Attributes:
        clickhouse (bool): Whether Clickhouse is reachable.
        postgres (bool): Whether Postgres is reachable.
        redis (bool): Whether Redis is reachable.
    """

    clickhouse: bool
    postgres: bool
    redis: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clickhouse = self.clickhouse

        postgres = self.postgres

        redis = self.redis

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clickhouse": clickhouse,
                "postgres": postgres,
                "redis": redis,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        clickhouse = d.pop("clickhouse")

        postgres = d.pop("postgres")

        redis = d.pop("redis")

        status_services = cls(
            clickhouse=clickhouse,
            postgres=postgres,
            redis=redis,
        )

        status_services.additional_properties = d
        return status_services

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
