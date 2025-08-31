from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RawWeaponInfoVerticalRecoilV2")


@_attrs_define
class RawWeaponInfoVerticalRecoilV2:
    """
    Attributes:
        range_ (Union[None, Unset, float, list[float]]):
        burst_exponent (Union[None, Unset, float]):
        burst_constant (Union[None, Unset, float]):
        burst_slope (Union[None, Unset, float]):
    """

    range_: Union[None, Unset, float, list[float]] = UNSET
    burst_exponent: Union[None, Unset, float] = UNSET
    burst_constant: Union[None, Unset, float] = UNSET
    burst_slope: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        range_: Union[None, Unset, float, list[float]]
        if isinstance(self.range_, Unset):
            range_ = UNSET
        elif isinstance(self.range_, list):
            range_ = self.range_

        else:
            range_ = self.range_

        burst_exponent: Union[None, Unset, float]
        if isinstance(self.burst_exponent, Unset):
            burst_exponent = UNSET
        else:
            burst_exponent = self.burst_exponent

        burst_constant: Union[None, Unset, float]
        if isinstance(self.burst_constant, Unset):
            burst_constant = UNSET
        else:
            burst_constant = self.burst_constant

        burst_slope: Union[None, Unset, float]
        if isinstance(self.burst_slope, Unset):
            burst_slope = UNSET
        else:
            burst_slope = self.burst_slope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if range_ is not UNSET:
            field_dict["range"] = range_
        if burst_exponent is not UNSET:
            field_dict["burst_exponent"] = burst_exponent
        if burst_constant is not UNSET:
            field_dict["burst_constant"] = burst_constant
        if burst_slope is not UNSET:
            field_dict["burst_slope"] = burst_slope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_range_(data: object) -> Union[None, Unset, float, list[float]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                range_type_0 = cast(list[float], data)

                return range_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, float, list[float]], data)

        range_ = _parse_range_(d.pop("range", UNSET))

        def _parse_burst_exponent(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        burst_exponent = _parse_burst_exponent(d.pop("burst_exponent", UNSET))

        def _parse_burst_constant(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        burst_constant = _parse_burst_constant(d.pop("burst_constant", UNSET))

        def _parse_burst_slope(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        burst_slope = _parse_burst_slope(d.pop("burst_slope", UNSET))

        raw_weapon_info_vertical_recoil_v2 = cls(
            range_=range_,
            burst_exponent=burst_exponent,
            burst_constant=burst_constant,
            burst_slope=burst_slope,
        )

        raw_weapon_info_vertical_recoil_v2.additional_properties = d
        return raw_weapon_info_vertical_recoil_v2

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
