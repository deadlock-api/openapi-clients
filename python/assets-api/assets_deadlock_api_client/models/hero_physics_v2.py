from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeroPhysicsV2")


@_attrs_define
class HeroPhysicsV2:
    """
    Attributes:
        collision_height (float):
        collision_radius (float):
        stealth_speed_meters_per_second (float):
        step_height (float):
        footstep_sound_travel_distance_meters (Union[None, Unset, float]):
        step_sound_time (Union[None, Unset, float]):
        step_sound_time_sprinting (Union[None, Unset, float]):
    """

    collision_height: float
    collision_radius: float
    stealth_speed_meters_per_second: float
    step_height: float
    footstep_sound_travel_distance_meters: Union[None, Unset, float] = UNSET
    step_sound_time: Union[None, Unset, float] = UNSET
    step_sound_time_sprinting: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collision_height = self.collision_height

        collision_radius = self.collision_radius

        stealth_speed_meters_per_second = self.stealth_speed_meters_per_second

        step_height = self.step_height

        footstep_sound_travel_distance_meters: Union[None, Unset, float]
        if isinstance(self.footstep_sound_travel_distance_meters, Unset):
            footstep_sound_travel_distance_meters = UNSET
        else:
            footstep_sound_travel_distance_meters = self.footstep_sound_travel_distance_meters

        step_sound_time: Union[None, Unset, float]
        if isinstance(self.step_sound_time, Unset):
            step_sound_time = UNSET
        else:
            step_sound_time = self.step_sound_time

        step_sound_time_sprinting: Union[None, Unset, float]
        if isinstance(self.step_sound_time_sprinting, Unset):
            step_sound_time_sprinting = UNSET
        else:
            step_sound_time_sprinting = self.step_sound_time_sprinting

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collision_height": collision_height,
                "collision_radius": collision_radius,
                "stealth_speed_meters_per_second": stealth_speed_meters_per_second,
                "step_height": step_height,
            }
        )
        if footstep_sound_travel_distance_meters is not UNSET:
            field_dict["footstep_sound_travel_distance_meters"] = footstep_sound_travel_distance_meters
        if step_sound_time is not UNSET:
            field_dict["step_sound_time"] = step_sound_time
        if step_sound_time_sprinting is not UNSET:
            field_dict["step_sound_time_sprinting"] = step_sound_time_sprinting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collision_height = d.pop("collision_height")

        collision_radius = d.pop("collision_radius")

        stealth_speed_meters_per_second = d.pop("stealth_speed_meters_per_second")

        step_height = d.pop("step_height")

        def _parse_footstep_sound_travel_distance_meters(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        footstep_sound_travel_distance_meters = _parse_footstep_sound_travel_distance_meters(
            d.pop("footstep_sound_travel_distance_meters", UNSET)
        )

        def _parse_step_sound_time(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        step_sound_time = _parse_step_sound_time(d.pop("step_sound_time", UNSET))

        def _parse_step_sound_time_sprinting(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        step_sound_time_sprinting = _parse_step_sound_time_sprinting(d.pop("step_sound_time_sprinting", UNSET))

        hero_physics_v2 = cls(
            collision_height=collision_height,
            collision_radius=collision_radius,
            stealth_speed_meters_per_second=stealth_speed_meters_per_second,
            step_height=step_height,
            footstep_sound_travel_distance_meters=footstep_sound_travel_distance_meters,
            step_sound_time=step_sound_time,
            step_sound_time_sprinting=step_sound_time_sprinting,
        )

        hero_physics_v2.additional_properties = d
        return hero_physics_v2

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
