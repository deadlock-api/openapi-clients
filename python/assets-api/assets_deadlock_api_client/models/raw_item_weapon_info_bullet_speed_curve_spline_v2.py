from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RawItemWeaponInfoBulletSpeedCurveSplineV2")


@_attrs_define
class RawItemWeaponInfoBulletSpeedCurveSplineV2:
    """
    Attributes:
        slope_incoming (float):
        slope_outgoing (float):
        x (float):
        y (float):
    """

    slope_incoming: float
    slope_outgoing: float
    x: float
    y: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slope_incoming = self.slope_incoming

        slope_outgoing = self.slope_outgoing

        x = self.x

        y = self.y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slope_incoming": slope_incoming,
                "slope_outgoing": slope_outgoing,
                "x": x,
                "y": y,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slope_incoming = d.pop("slope_incoming")

        slope_outgoing = d.pop("slope_outgoing")

        x = d.pop("x")

        y = d.pop("y")

        raw_item_weapon_info_bullet_speed_curve_spline_v2 = cls(
            slope_incoming=slope_incoming,
            slope_outgoing=slope_outgoing,
            x=x,
            y=y,
        )

        raw_item_weapon_info_bullet_speed_curve_spline_v2.additional_properties = d
        return raw_item_weapon_info_bullet_speed_curve_spline_v2

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
