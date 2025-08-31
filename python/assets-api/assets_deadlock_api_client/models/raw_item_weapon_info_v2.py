from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.raw_item_weapon_info_bullet_speed_curve_v2 import RawItemWeaponInfoBulletSpeedCurveV2


T = TypeVar("T", bound="RawItemWeaponInfoV2")


@_attrs_define
class RawItemWeaponInfoV2:
    """
    Attributes:
        bullet_speed_curve (Union['RawItemWeaponInfoBulletSpeedCurveV2', None, Unset]):
    """

    bullet_speed_curve: Union["RawItemWeaponInfoBulletSpeedCurveV2", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.raw_item_weapon_info_bullet_speed_curve_v2 import RawItemWeaponInfoBulletSpeedCurveV2

        bullet_speed_curve: Union[None, Unset, dict[str, Any]]
        if isinstance(self.bullet_speed_curve, Unset):
            bullet_speed_curve = UNSET
        elif isinstance(self.bullet_speed_curve, RawItemWeaponInfoBulletSpeedCurveV2):
            bullet_speed_curve = self.bullet_speed_curve.to_dict()
        else:
            bullet_speed_curve = self.bullet_speed_curve

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bullet_speed_curve is not UNSET:
            field_dict["bullet_speed_curve"] = bullet_speed_curve

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_item_weapon_info_bullet_speed_curve_v2 import RawItemWeaponInfoBulletSpeedCurveV2

        d = dict(src_dict)

        def _parse_bullet_speed_curve(data: object) -> Union["RawItemWeaponInfoBulletSpeedCurveV2", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bullet_speed_curve_type_0 = RawItemWeaponInfoBulletSpeedCurveV2.from_dict(data)

                return bullet_speed_curve_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RawItemWeaponInfoBulletSpeedCurveV2", None, Unset], data)

        bullet_speed_curve = _parse_bullet_speed_curve(d.pop("bullet_speed_curve", UNSET))

        raw_item_weapon_info_v2 = cls(
            bullet_speed_curve=bullet_speed_curve,
        )

        raw_item_weapon_info_v2.additional_properties = d
        return raw_item_weapon_info_v2

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
