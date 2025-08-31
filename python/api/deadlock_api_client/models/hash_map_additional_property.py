from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HashMapAdditionalProperty")


@_attrs_define
class HashMapAdditionalProperty:
    """
    Attributes:
        avg (float):
        percentile1 (float):
        percentile10 (float):
        percentile25 (float):
        percentile5 (float):
        percentile50 (float):
        percentile75 (float):
        percentile90 (float):
        percentile95 (float):
        percentile99 (float):
        std (float):
    """

    avg: float
    percentile1: float
    percentile10: float
    percentile25: float
    percentile5: float
    percentile50: float
    percentile75: float
    percentile90: float
    percentile95: float
    percentile99: float
    std: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg = self.avg

        percentile1 = self.percentile1

        percentile10 = self.percentile10

        percentile25 = self.percentile25

        percentile5 = self.percentile5

        percentile50 = self.percentile50

        percentile75 = self.percentile75

        percentile90 = self.percentile90

        percentile95 = self.percentile95

        percentile99 = self.percentile99

        std = self.std

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avg": avg,
                "percentile1": percentile1,
                "percentile10": percentile10,
                "percentile25": percentile25,
                "percentile5": percentile5,
                "percentile50": percentile50,
                "percentile75": percentile75,
                "percentile90": percentile90,
                "percentile95": percentile95,
                "percentile99": percentile99,
                "std": std,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg = d.pop("avg")

        percentile1 = d.pop("percentile1")

        percentile10 = d.pop("percentile10")

        percentile25 = d.pop("percentile25")

        percentile5 = d.pop("percentile5")

        percentile50 = d.pop("percentile50")

        percentile75 = d.pop("percentile75")

        percentile90 = d.pop("percentile90")

        percentile95 = d.pop("percentile95")

        percentile99 = d.pop("percentile99")

        std = d.pop("std")

        hash_map_additional_property = cls(
            avg=avg,
            percentile1=percentile1,
            percentile10=percentile10,
            percentile25=percentile25,
            percentile5=percentile5,
            percentile50=percentile50,
            percentile75=percentile75,
            percentile90=percentile90,
            percentile95=percentile95,
            percentile99=percentile99,
            std=std,
        )

        hash_map_additional_property.additional_properties = d
        return hash_map_additional_property

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
