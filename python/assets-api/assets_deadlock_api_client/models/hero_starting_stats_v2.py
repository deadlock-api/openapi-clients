from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hero_starting_stat_v2 import HeroStartingStatV2


T = TypeVar("T", bound="HeroStartingStatsV2")


@_attrs_define
class HeroStartingStatsV2:
    """
    Attributes:
        max_move_speed (HeroStartingStatV2):
        sprint_speed (HeroStartingStatV2):
        crouch_speed (HeroStartingStatV2):
        move_acceleration (HeroStartingStatV2):
        light_melee_damage (HeroStartingStatV2):
        heavy_melee_damage (HeroStartingStatV2):
        max_health (HeroStartingStatV2):
        weapon_power (HeroStartingStatV2):
        reload_speed (HeroStartingStatV2):
        weapon_power_scale (HeroStartingStatV2):
        proc_build_up_rate_scale (HeroStartingStatV2):
        stamina (HeroStartingStatV2):
        base_health_regen (HeroStartingStatV2):
        stamina_regen_per_second (HeroStartingStatV2):
        ability_resource_max (HeroStartingStatV2):
        ability_resource_regen_per_second (HeroStartingStatV2):
        crit_damage_received_scale (HeroStartingStatV2):
        tech_duration (HeroStartingStatV2):
        tech_range (HeroStartingStatV2):
        tech_armor_damage_reduction (Union['HeroStartingStatV2', None, Unset]):
        bullet_armor_damage_reduction (Union['HeroStartingStatV2', None, Unset]):
    """

    max_move_speed: "HeroStartingStatV2"
    sprint_speed: "HeroStartingStatV2"
    crouch_speed: "HeroStartingStatV2"
    move_acceleration: "HeroStartingStatV2"
    light_melee_damage: "HeroStartingStatV2"
    heavy_melee_damage: "HeroStartingStatV2"
    max_health: "HeroStartingStatV2"
    weapon_power: "HeroStartingStatV2"
    reload_speed: "HeroStartingStatV2"
    weapon_power_scale: "HeroStartingStatV2"
    proc_build_up_rate_scale: "HeroStartingStatV2"
    stamina: "HeroStartingStatV2"
    base_health_regen: "HeroStartingStatV2"
    stamina_regen_per_second: "HeroStartingStatV2"
    ability_resource_max: "HeroStartingStatV2"
    ability_resource_regen_per_second: "HeroStartingStatV2"
    crit_damage_received_scale: "HeroStartingStatV2"
    tech_duration: "HeroStartingStatV2"
    tech_range: "HeroStartingStatV2"
    tech_armor_damage_reduction: Union["HeroStartingStatV2", None, Unset] = UNSET
    bullet_armor_damage_reduction: Union["HeroStartingStatV2", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hero_starting_stat_v2 import HeroStartingStatV2

        max_move_speed = self.max_move_speed.to_dict()

        sprint_speed = self.sprint_speed.to_dict()

        crouch_speed = self.crouch_speed.to_dict()

        move_acceleration = self.move_acceleration.to_dict()

        light_melee_damage = self.light_melee_damage.to_dict()

        heavy_melee_damage = self.heavy_melee_damage.to_dict()

        max_health = self.max_health.to_dict()

        weapon_power = self.weapon_power.to_dict()

        reload_speed = self.reload_speed.to_dict()

        weapon_power_scale = self.weapon_power_scale.to_dict()

        proc_build_up_rate_scale = self.proc_build_up_rate_scale.to_dict()

        stamina = self.stamina.to_dict()

        base_health_regen = self.base_health_regen.to_dict()

        stamina_regen_per_second = self.stamina_regen_per_second.to_dict()

        ability_resource_max = self.ability_resource_max.to_dict()

        ability_resource_regen_per_second = self.ability_resource_regen_per_second.to_dict()

        crit_damage_received_scale = self.crit_damage_received_scale.to_dict()

        tech_duration = self.tech_duration.to_dict()

        tech_range = self.tech_range.to_dict()

        tech_armor_damage_reduction: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tech_armor_damage_reduction, Unset):
            tech_armor_damage_reduction = UNSET
        elif isinstance(self.tech_armor_damage_reduction, HeroStartingStatV2):
            tech_armor_damage_reduction = self.tech_armor_damage_reduction.to_dict()
        else:
            tech_armor_damage_reduction = self.tech_armor_damage_reduction

        bullet_armor_damage_reduction: Union[None, Unset, dict[str, Any]]
        if isinstance(self.bullet_armor_damage_reduction, Unset):
            bullet_armor_damage_reduction = UNSET
        elif isinstance(self.bullet_armor_damage_reduction, HeroStartingStatV2):
            bullet_armor_damage_reduction = self.bullet_armor_damage_reduction.to_dict()
        else:
            bullet_armor_damage_reduction = self.bullet_armor_damage_reduction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max_move_speed": max_move_speed,
                "sprint_speed": sprint_speed,
                "crouch_speed": crouch_speed,
                "move_acceleration": move_acceleration,
                "light_melee_damage": light_melee_damage,
                "heavy_melee_damage": heavy_melee_damage,
                "max_health": max_health,
                "weapon_power": weapon_power,
                "reload_speed": reload_speed,
                "weapon_power_scale": weapon_power_scale,
                "proc_build_up_rate_scale": proc_build_up_rate_scale,
                "stamina": stamina,
                "base_health_regen": base_health_regen,
                "stamina_regen_per_second": stamina_regen_per_second,
                "ability_resource_max": ability_resource_max,
                "ability_resource_regen_per_second": ability_resource_regen_per_second,
                "crit_damage_received_scale": crit_damage_received_scale,
                "tech_duration": tech_duration,
                "tech_range": tech_range,
            }
        )
        if tech_armor_damage_reduction is not UNSET:
            field_dict["tech_armor_damage_reduction"] = tech_armor_damage_reduction
        if bullet_armor_damage_reduction is not UNSET:
            field_dict["bullet_armor_damage_reduction"] = bullet_armor_damage_reduction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hero_starting_stat_v2 import HeroStartingStatV2

        d = dict(src_dict)
        max_move_speed = HeroStartingStatV2.from_dict(d.pop("max_move_speed"))

        sprint_speed = HeroStartingStatV2.from_dict(d.pop("sprint_speed"))

        crouch_speed = HeroStartingStatV2.from_dict(d.pop("crouch_speed"))

        move_acceleration = HeroStartingStatV2.from_dict(d.pop("move_acceleration"))

        light_melee_damage = HeroStartingStatV2.from_dict(d.pop("light_melee_damage"))

        heavy_melee_damage = HeroStartingStatV2.from_dict(d.pop("heavy_melee_damage"))

        max_health = HeroStartingStatV2.from_dict(d.pop("max_health"))

        weapon_power = HeroStartingStatV2.from_dict(d.pop("weapon_power"))

        reload_speed = HeroStartingStatV2.from_dict(d.pop("reload_speed"))

        weapon_power_scale = HeroStartingStatV2.from_dict(d.pop("weapon_power_scale"))

        proc_build_up_rate_scale = HeroStartingStatV2.from_dict(d.pop("proc_build_up_rate_scale"))

        stamina = HeroStartingStatV2.from_dict(d.pop("stamina"))

        base_health_regen = HeroStartingStatV2.from_dict(d.pop("base_health_regen"))

        stamina_regen_per_second = HeroStartingStatV2.from_dict(d.pop("stamina_regen_per_second"))

        ability_resource_max = HeroStartingStatV2.from_dict(d.pop("ability_resource_max"))

        ability_resource_regen_per_second = HeroStartingStatV2.from_dict(d.pop("ability_resource_regen_per_second"))

        crit_damage_received_scale = HeroStartingStatV2.from_dict(d.pop("crit_damage_received_scale"))

        tech_duration = HeroStartingStatV2.from_dict(d.pop("tech_duration"))

        tech_range = HeroStartingStatV2.from_dict(d.pop("tech_range"))

        def _parse_tech_armor_damage_reduction(data: object) -> Union["HeroStartingStatV2", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tech_armor_damage_reduction_type_0 = HeroStartingStatV2.from_dict(data)

                return tech_armor_damage_reduction_type_0
            except:  # noqa: E722
                pass
            return cast(Union["HeroStartingStatV2", None, Unset], data)

        tech_armor_damage_reduction = _parse_tech_armor_damage_reduction(d.pop("tech_armor_damage_reduction", UNSET))

        def _parse_bullet_armor_damage_reduction(data: object) -> Union["HeroStartingStatV2", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bullet_armor_damage_reduction_type_0 = HeroStartingStatV2.from_dict(data)

                return bullet_armor_damage_reduction_type_0
            except:  # noqa: E722
                pass
            return cast(Union["HeroStartingStatV2", None, Unset], data)

        bullet_armor_damage_reduction = _parse_bullet_armor_damage_reduction(
            d.pop("bullet_armor_damage_reduction", UNSET)
        )

        hero_starting_stats_v2 = cls(
            max_move_speed=max_move_speed,
            sprint_speed=sprint_speed,
            crouch_speed=crouch_speed,
            move_acceleration=move_acceleration,
            light_melee_damage=light_melee_damage,
            heavy_melee_damage=heavy_melee_damage,
            max_health=max_health,
            weapon_power=weapon_power,
            reload_speed=reload_speed,
            weapon_power_scale=weapon_power_scale,
            proc_build_up_rate_scale=proc_build_up_rate_scale,
            stamina=stamina,
            base_health_regen=base_health_regen,
            stamina_regen_per_second=stamina_regen_per_second,
            ability_resource_max=ability_resource_max,
            ability_resource_regen_per_second=ability_resource_regen_per_second,
            crit_damage_received_scale=crit_damage_received_scale,
            tech_duration=tech_duration,
            tech_range=tech_range,
            tech_armor_damage_reduction=tech_armor_damage_reduction,
            bullet_armor_damage_reduction=bullet_armor_damage_reduction,
        )

        hero_starting_stats_v2.additional_properties = d
        return hero_starting_stats_v2

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
