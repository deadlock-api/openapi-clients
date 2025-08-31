from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.raw_item_weapon_info_bullet_speed_curve_spline_v2 import RawItemWeaponInfoBulletSpeedCurveSplineV2


T = TypeVar("T", bound="RawItemWeaponInfoBulletSpeedCurveV2")


@_attrs_define
class RawItemWeaponInfoBulletSpeedCurveV2:
    """
    Attributes:
        domain_maxs (list[float]):
        domain_mins (list[float]):
        spline (Union[Unset, list['RawItemWeaponInfoBulletSpeedCurveSplineV2']]):
    """

    domain_maxs: list[float]
    domain_mins: list[float]
    spline: Union[Unset, list["RawItemWeaponInfoBulletSpeedCurveSplineV2"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_maxs = self.domain_maxs

        domain_mins = self.domain_mins

        spline: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.spline, Unset):
            spline = []
            for spline_item_data in self.spline:
                spline_item = spline_item_data.to_dict()
                spline.append(spline_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain_maxs": domain_maxs,
                "domain_mins": domain_mins,
            }
        )
        if spline is not UNSET:
            field_dict["spline"] = spline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_item_weapon_info_bullet_speed_curve_spline_v2 import RawItemWeaponInfoBulletSpeedCurveSplineV2

        d = dict(src_dict)
        domain_maxs = cast(list[float], d.pop("domain_maxs"))

        domain_mins = cast(list[float], d.pop("domain_mins"))

        spline = []
        _spline = d.pop("spline", UNSET)
        for spline_item_data in _spline or []:
            spline_item = RawItemWeaponInfoBulletSpeedCurveSplineV2.from_dict(spline_item_data)

            spline.append(spline_item)

        raw_item_weapon_info_bullet_speed_curve_v2 = cls(
            domain_maxs=domain_maxs,
            domain_mins=domain_mins,
            spline=spline,
        )

        raw_item_weapon_info_bullet_speed_curve_v2.additional_properties = d
        return raw_item_weapon_info_bullet_speed_curve_v2

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
