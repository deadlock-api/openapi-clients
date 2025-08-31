from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.raw_item_weapon_info_bullet_speed_curve_v2 import RawItemWeaponInfoBulletSpeedCurveV2
    from ..models.raw_weapon_info_horizontal_recoil_v2 import RawWeaponInfoHorizontalRecoilV2
    from ..models.raw_weapon_info_vertical_recoil_v2 import RawWeaponInfoVerticalRecoilV2


T = TypeVar("T", bound="RawWeaponInfoV2")


@_attrs_define
class RawWeaponInfoV2:
    """
    Attributes:
        can_zoom (Union[None, Unset, bool]):
        bullet_damage (Union[None, Unset, float]):
        bullet_gravity_scale (Union[None, Unset, float]):
        bullet_inherit_shooter_velocity_scale (Union[None, Unset, float]):
        bullet_lifetime (Union[None, Unset, float]):
        bullet_radius (Union[None, Unset, float]):
        bullet_radius_vs_world (Union[None, Unset, float]):
        bullet_reflect_amount (Union[None, Unset, float]):
        bullet_reflect_scale (Union[None, Unset, float]):
        bullet_whiz_distance (Union[None, Unset, float]):
        burst_shot_cooldown (Union[None, Unset, float]):
        crit_bonus_against_npcs (Union[None, Unset, float]):
        crit_bonus_end (Union[None, Unset, float]):
        crit_bonus_end_range (Union[None, Unset, float]):
        crit_bonus_start (Union[None, Unset, float]):
        crit_bonus_start_range (Union[None, Unset, float]):
        cycle_time (Union[None, Unset, float]):
        intra_burst_cycle_time (Union[None, Unset, float]):
        max_spin_cycle_time (Union[None, Unset, float]):
        damage_falloff_bias (Union[None, Unset, float]):
        damage_falloff_end_range (Union[None, Unset, float]):
        damage_falloff_end_scale (Union[None, Unset, float]):
        damage_falloff_start_range (Union[None, Unset, float]):
        damage_falloff_start_scale (Union[None, Unset, float]):
        horizontal_punch (Union[None, Unset, float]):
        range_ (Union[None, Unset, float]):
        recoil_recovery_delay_factor (Union[None, Unset, float]):
        recoil_recovery_speed (Union[None, Unset, float]):
        recoil_shot_index_recovery_time_factor (Union[None, Unset, float]):
        recoil_speed (Union[None, Unset, float]):
        reload_move_speed (Union[None, Unset, float]):
        scatter_yaw_scale (Union[None, Unset, float]):
        aiming_shot_spread_penalty (Union[None, Unset, list[float], str]):
        standing_shot_spread_penalty (Union[None, Unset, list[float], str]):
        shoot_move_speed_percent (Union[None, Unset, float]):
        shoot_spread_penalty_decay (Union[None, Unset, float]):
        shoot_spread_penalty_decay_delay (Union[None, Unset, float]):
        shoot_spread_penalty_per_shot (Union[None, Unset, float]):
        shooting_up_spread_penalty (Union[None, Unset, float]):
        vertical_punch (Union[None, Unset, float]):
        zoom_fov (Union[None, Unset, float]):
        zoom_move_speed_percent (Union[None, Unset, float]):
        bullets (Union[None, Unset, int]):
        burst_shot_count (Union[None, Unset, int]):
        clip_size (Union[None, Unset, int]):
        spread (Union[None, Unset, float]):
        standing_spread (Union[None, Unset, float]):
        low_ammo_indicator_threshold (Union[None, Unset, float]):
        recoil_seed (Union[None, Unset, float]):
        reload_duration (Union[None, Unset, float]):
        bullet_speed_curve (Union['RawItemWeaponInfoBulletSpeedCurveV2', None, Unset]):
        horizontal_recoil (Union['RawWeaponInfoHorizontalRecoilV2', None, Unset]):
        vertical_recoil (Union['RawWeaponInfoVerticalRecoilV2', None, Unset]):
    """

    can_zoom: Union[None, Unset, bool] = UNSET
    bullet_damage: Union[None, Unset, float] = UNSET
    bullet_gravity_scale: Union[None, Unset, float] = UNSET
    bullet_inherit_shooter_velocity_scale: Union[None, Unset, float] = UNSET
    bullet_lifetime: Union[None, Unset, float] = UNSET
    bullet_radius: Union[None, Unset, float] = UNSET
    bullet_radius_vs_world: Union[None, Unset, float] = UNSET
    bullet_reflect_amount: Union[None, Unset, float] = UNSET
    bullet_reflect_scale: Union[None, Unset, float] = UNSET
    bullet_whiz_distance: Union[None, Unset, float] = UNSET
    burst_shot_cooldown: Union[None, Unset, float] = UNSET
    crit_bonus_against_npcs: Union[None, Unset, float] = UNSET
    crit_bonus_end: Union[None, Unset, float] = UNSET
    crit_bonus_end_range: Union[None, Unset, float] = UNSET
    crit_bonus_start: Union[None, Unset, float] = UNSET
    crit_bonus_start_range: Union[None, Unset, float] = UNSET
    cycle_time: Union[None, Unset, float] = UNSET
    intra_burst_cycle_time: Union[None, Unset, float] = UNSET
    max_spin_cycle_time: Union[None, Unset, float] = UNSET
    damage_falloff_bias: Union[None, Unset, float] = UNSET
    damage_falloff_end_range: Union[None, Unset, float] = UNSET
    damage_falloff_end_scale: Union[None, Unset, float] = UNSET
    damage_falloff_start_range: Union[None, Unset, float] = UNSET
    damage_falloff_start_scale: Union[None, Unset, float] = UNSET
    horizontal_punch: Union[None, Unset, float] = UNSET
    range_: Union[None, Unset, float] = UNSET
    recoil_recovery_delay_factor: Union[None, Unset, float] = UNSET
    recoil_recovery_speed: Union[None, Unset, float] = UNSET
    recoil_shot_index_recovery_time_factor: Union[None, Unset, float] = UNSET
    recoil_speed: Union[None, Unset, float] = UNSET
    reload_move_speed: Union[None, Unset, float] = UNSET
    scatter_yaw_scale: Union[None, Unset, float] = UNSET
    aiming_shot_spread_penalty: Union[None, Unset, list[float], str] = UNSET
    standing_shot_spread_penalty: Union[None, Unset, list[float], str] = UNSET
    shoot_move_speed_percent: Union[None, Unset, float] = UNSET
    shoot_spread_penalty_decay: Union[None, Unset, float] = UNSET
    shoot_spread_penalty_decay_delay: Union[None, Unset, float] = UNSET
    shoot_spread_penalty_per_shot: Union[None, Unset, float] = UNSET
    shooting_up_spread_penalty: Union[None, Unset, float] = UNSET
    vertical_punch: Union[None, Unset, float] = UNSET
    zoom_fov: Union[None, Unset, float] = UNSET
    zoom_move_speed_percent: Union[None, Unset, float] = UNSET
    bullets: Union[None, Unset, int] = UNSET
    burst_shot_count: Union[None, Unset, int] = UNSET
    clip_size: Union[None, Unset, int] = UNSET
    spread: Union[None, Unset, float] = UNSET
    standing_spread: Union[None, Unset, float] = UNSET
    low_ammo_indicator_threshold: Union[None, Unset, float] = UNSET
    recoil_seed: Union[None, Unset, float] = UNSET
    reload_duration: Union[None, Unset, float] = UNSET
    bullet_speed_curve: Union["RawItemWeaponInfoBulletSpeedCurveV2", None, Unset] = UNSET
    horizontal_recoil: Union["RawWeaponInfoHorizontalRecoilV2", None, Unset] = UNSET
    vertical_recoil: Union["RawWeaponInfoVerticalRecoilV2", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.raw_item_weapon_info_bullet_speed_curve_v2 import RawItemWeaponInfoBulletSpeedCurveV2
        from ..models.raw_weapon_info_horizontal_recoil_v2 import RawWeaponInfoHorizontalRecoilV2
        from ..models.raw_weapon_info_vertical_recoil_v2 import RawWeaponInfoVerticalRecoilV2

        can_zoom: Union[None, Unset, bool]
        if isinstance(self.can_zoom, Unset):
            can_zoom = UNSET
        else:
            can_zoom = self.can_zoom

        bullet_damage: Union[None, Unset, float]
        if isinstance(self.bullet_damage, Unset):
            bullet_damage = UNSET
        else:
            bullet_damage = self.bullet_damage

        bullet_gravity_scale: Union[None, Unset, float]
        if isinstance(self.bullet_gravity_scale, Unset):
            bullet_gravity_scale = UNSET
        else:
            bullet_gravity_scale = self.bullet_gravity_scale

        bullet_inherit_shooter_velocity_scale: Union[None, Unset, float]
        if isinstance(self.bullet_inherit_shooter_velocity_scale, Unset):
            bullet_inherit_shooter_velocity_scale = UNSET
        else:
            bullet_inherit_shooter_velocity_scale = self.bullet_inherit_shooter_velocity_scale

        bullet_lifetime: Union[None, Unset, float]
        if isinstance(self.bullet_lifetime, Unset):
            bullet_lifetime = UNSET
        else:
            bullet_lifetime = self.bullet_lifetime

        bullet_radius: Union[None, Unset, float]
        if isinstance(self.bullet_radius, Unset):
            bullet_radius = UNSET
        else:
            bullet_radius = self.bullet_radius

        bullet_radius_vs_world: Union[None, Unset, float]
        if isinstance(self.bullet_radius_vs_world, Unset):
            bullet_radius_vs_world = UNSET
        else:
            bullet_radius_vs_world = self.bullet_radius_vs_world

        bullet_reflect_amount: Union[None, Unset, float]
        if isinstance(self.bullet_reflect_amount, Unset):
            bullet_reflect_amount = UNSET
        else:
            bullet_reflect_amount = self.bullet_reflect_amount

        bullet_reflect_scale: Union[None, Unset, float]
        if isinstance(self.bullet_reflect_scale, Unset):
            bullet_reflect_scale = UNSET
        else:
            bullet_reflect_scale = self.bullet_reflect_scale

        bullet_whiz_distance: Union[None, Unset, float]
        if isinstance(self.bullet_whiz_distance, Unset):
            bullet_whiz_distance = UNSET
        else:
            bullet_whiz_distance = self.bullet_whiz_distance

        burst_shot_cooldown: Union[None, Unset, float]
        if isinstance(self.burst_shot_cooldown, Unset):
            burst_shot_cooldown = UNSET
        else:
            burst_shot_cooldown = self.burst_shot_cooldown

        crit_bonus_against_npcs: Union[None, Unset, float]
        if isinstance(self.crit_bonus_against_npcs, Unset):
            crit_bonus_against_npcs = UNSET
        else:
            crit_bonus_against_npcs = self.crit_bonus_against_npcs

        crit_bonus_end: Union[None, Unset, float]
        if isinstance(self.crit_bonus_end, Unset):
            crit_bonus_end = UNSET
        else:
            crit_bonus_end = self.crit_bonus_end

        crit_bonus_end_range: Union[None, Unset, float]
        if isinstance(self.crit_bonus_end_range, Unset):
            crit_bonus_end_range = UNSET
        else:
            crit_bonus_end_range = self.crit_bonus_end_range

        crit_bonus_start: Union[None, Unset, float]
        if isinstance(self.crit_bonus_start, Unset):
            crit_bonus_start = UNSET
        else:
            crit_bonus_start = self.crit_bonus_start

        crit_bonus_start_range: Union[None, Unset, float]
        if isinstance(self.crit_bonus_start_range, Unset):
            crit_bonus_start_range = UNSET
        else:
            crit_bonus_start_range = self.crit_bonus_start_range

        cycle_time: Union[None, Unset, float]
        if isinstance(self.cycle_time, Unset):
            cycle_time = UNSET
        else:
            cycle_time = self.cycle_time

        intra_burst_cycle_time: Union[None, Unset, float]
        if isinstance(self.intra_burst_cycle_time, Unset):
            intra_burst_cycle_time = UNSET
        else:
            intra_burst_cycle_time = self.intra_burst_cycle_time

        max_spin_cycle_time: Union[None, Unset, float]
        if isinstance(self.max_spin_cycle_time, Unset):
            max_spin_cycle_time = UNSET
        else:
            max_spin_cycle_time = self.max_spin_cycle_time

        damage_falloff_bias: Union[None, Unset, float]
        if isinstance(self.damage_falloff_bias, Unset):
            damage_falloff_bias = UNSET
        else:
            damage_falloff_bias = self.damage_falloff_bias

        damage_falloff_end_range: Union[None, Unset, float]
        if isinstance(self.damage_falloff_end_range, Unset):
            damage_falloff_end_range = UNSET
        else:
            damage_falloff_end_range = self.damage_falloff_end_range

        damage_falloff_end_scale: Union[None, Unset, float]
        if isinstance(self.damage_falloff_end_scale, Unset):
            damage_falloff_end_scale = UNSET
        else:
            damage_falloff_end_scale = self.damage_falloff_end_scale

        damage_falloff_start_range: Union[None, Unset, float]
        if isinstance(self.damage_falloff_start_range, Unset):
            damage_falloff_start_range = UNSET
        else:
            damage_falloff_start_range = self.damage_falloff_start_range

        damage_falloff_start_scale: Union[None, Unset, float]
        if isinstance(self.damage_falloff_start_scale, Unset):
            damage_falloff_start_scale = UNSET
        else:
            damage_falloff_start_scale = self.damage_falloff_start_scale

        horizontal_punch: Union[None, Unset, float]
        if isinstance(self.horizontal_punch, Unset):
            horizontal_punch = UNSET
        else:
            horizontal_punch = self.horizontal_punch

        range_: Union[None, Unset, float]
        if isinstance(self.range_, Unset):
            range_ = UNSET
        else:
            range_ = self.range_

        recoil_recovery_delay_factor: Union[None, Unset, float]
        if isinstance(self.recoil_recovery_delay_factor, Unset):
            recoil_recovery_delay_factor = UNSET
        else:
            recoil_recovery_delay_factor = self.recoil_recovery_delay_factor

        recoil_recovery_speed: Union[None, Unset, float]
        if isinstance(self.recoil_recovery_speed, Unset):
            recoil_recovery_speed = UNSET
        else:
            recoil_recovery_speed = self.recoil_recovery_speed

        recoil_shot_index_recovery_time_factor: Union[None, Unset, float]
        if isinstance(self.recoil_shot_index_recovery_time_factor, Unset):
            recoil_shot_index_recovery_time_factor = UNSET
        else:
            recoil_shot_index_recovery_time_factor = self.recoil_shot_index_recovery_time_factor

        recoil_speed: Union[None, Unset, float]
        if isinstance(self.recoil_speed, Unset):
            recoil_speed = UNSET
        else:
            recoil_speed = self.recoil_speed

        reload_move_speed: Union[None, Unset, float]
        if isinstance(self.reload_move_speed, Unset):
            reload_move_speed = UNSET
        else:
            reload_move_speed = self.reload_move_speed

        scatter_yaw_scale: Union[None, Unset, float]
        if isinstance(self.scatter_yaw_scale, Unset):
            scatter_yaw_scale = UNSET
        else:
            scatter_yaw_scale = self.scatter_yaw_scale

        aiming_shot_spread_penalty: Union[None, Unset, list[float], str]
        if isinstance(self.aiming_shot_spread_penalty, Unset):
            aiming_shot_spread_penalty = UNSET
        elif isinstance(self.aiming_shot_spread_penalty, list):
            aiming_shot_spread_penalty = self.aiming_shot_spread_penalty

        else:
            aiming_shot_spread_penalty = self.aiming_shot_spread_penalty

        standing_shot_spread_penalty: Union[None, Unset, list[float], str]
        if isinstance(self.standing_shot_spread_penalty, Unset):
            standing_shot_spread_penalty = UNSET
        elif isinstance(self.standing_shot_spread_penalty, list):
            standing_shot_spread_penalty = self.standing_shot_spread_penalty

        else:
            standing_shot_spread_penalty = self.standing_shot_spread_penalty

        shoot_move_speed_percent: Union[None, Unset, float]
        if isinstance(self.shoot_move_speed_percent, Unset):
            shoot_move_speed_percent = UNSET
        else:
            shoot_move_speed_percent = self.shoot_move_speed_percent

        shoot_spread_penalty_decay: Union[None, Unset, float]
        if isinstance(self.shoot_spread_penalty_decay, Unset):
            shoot_spread_penalty_decay = UNSET
        else:
            shoot_spread_penalty_decay = self.shoot_spread_penalty_decay

        shoot_spread_penalty_decay_delay: Union[None, Unset, float]
        if isinstance(self.shoot_spread_penalty_decay_delay, Unset):
            shoot_spread_penalty_decay_delay = UNSET
        else:
            shoot_spread_penalty_decay_delay = self.shoot_spread_penalty_decay_delay

        shoot_spread_penalty_per_shot: Union[None, Unset, float]
        if isinstance(self.shoot_spread_penalty_per_shot, Unset):
            shoot_spread_penalty_per_shot = UNSET
        else:
            shoot_spread_penalty_per_shot = self.shoot_spread_penalty_per_shot

        shooting_up_spread_penalty: Union[None, Unset, float]
        if isinstance(self.shooting_up_spread_penalty, Unset):
            shooting_up_spread_penalty = UNSET
        else:
            shooting_up_spread_penalty = self.shooting_up_spread_penalty

        vertical_punch: Union[None, Unset, float]
        if isinstance(self.vertical_punch, Unset):
            vertical_punch = UNSET
        else:
            vertical_punch = self.vertical_punch

        zoom_fov: Union[None, Unset, float]
        if isinstance(self.zoom_fov, Unset):
            zoom_fov = UNSET
        else:
            zoom_fov = self.zoom_fov

        zoom_move_speed_percent: Union[None, Unset, float]
        if isinstance(self.zoom_move_speed_percent, Unset):
            zoom_move_speed_percent = UNSET
        else:
            zoom_move_speed_percent = self.zoom_move_speed_percent

        bullets: Union[None, Unset, int]
        if isinstance(self.bullets, Unset):
            bullets = UNSET
        else:
            bullets = self.bullets

        burst_shot_count: Union[None, Unset, int]
        if isinstance(self.burst_shot_count, Unset):
            burst_shot_count = UNSET
        else:
            burst_shot_count = self.burst_shot_count

        clip_size: Union[None, Unset, int]
        if isinstance(self.clip_size, Unset):
            clip_size = UNSET
        else:
            clip_size = self.clip_size

        spread: Union[None, Unset, float]
        if isinstance(self.spread, Unset):
            spread = UNSET
        else:
            spread = self.spread

        standing_spread: Union[None, Unset, float]
        if isinstance(self.standing_spread, Unset):
            standing_spread = UNSET
        else:
            standing_spread = self.standing_spread

        low_ammo_indicator_threshold: Union[None, Unset, float]
        if isinstance(self.low_ammo_indicator_threshold, Unset):
            low_ammo_indicator_threshold = UNSET
        else:
            low_ammo_indicator_threshold = self.low_ammo_indicator_threshold

        recoil_seed: Union[None, Unset, float]
        if isinstance(self.recoil_seed, Unset):
            recoil_seed = UNSET
        else:
            recoil_seed = self.recoil_seed

        reload_duration: Union[None, Unset, float]
        if isinstance(self.reload_duration, Unset):
            reload_duration = UNSET
        else:
            reload_duration = self.reload_duration

        bullet_speed_curve: Union[None, Unset, dict[str, Any]]
        if isinstance(self.bullet_speed_curve, Unset):
            bullet_speed_curve = UNSET
        elif isinstance(self.bullet_speed_curve, RawItemWeaponInfoBulletSpeedCurveV2):
            bullet_speed_curve = self.bullet_speed_curve.to_dict()
        else:
            bullet_speed_curve = self.bullet_speed_curve

        horizontal_recoil: Union[None, Unset, dict[str, Any]]
        if isinstance(self.horizontal_recoil, Unset):
            horizontal_recoil = UNSET
        elif isinstance(self.horizontal_recoil, RawWeaponInfoHorizontalRecoilV2):
            horizontal_recoil = self.horizontal_recoil.to_dict()
        else:
            horizontal_recoil = self.horizontal_recoil

        vertical_recoil: Union[None, Unset, dict[str, Any]]
        if isinstance(self.vertical_recoil, Unset):
            vertical_recoil = UNSET
        elif isinstance(self.vertical_recoil, RawWeaponInfoVerticalRecoilV2):
            vertical_recoil = self.vertical_recoil.to_dict()
        else:
            vertical_recoil = self.vertical_recoil

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_zoom is not UNSET:
            field_dict["can_zoom"] = can_zoom
        if bullet_damage is not UNSET:
            field_dict["bullet_damage"] = bullet_damage
        if bullet_gravity_scale is not UNSET:
            field_dict["bullet_gravity_scale"] = bullet_gravity_scale
        if bullet_inherit_shooter_velocity_scale is not UNSET:
            field_dict["bullet_inherit_shooter_velocity_scale"] = bullet_inherit_shooter_velocity_scale
        if bullet_lifetime is not UNSET:
            field_dict["bullet_lifetime"] = bullet_lifetime
        if bullet_radius is not UNSET:
            field_dict["bullet_radius"] = bullet_radius
        if bullet_radius_vs_world is not UNSET:
            field_dict["bullet_radius_vs_world"] = bullet_radius_vs_world
        if bullet_reflect_amount is not UNSET:
            field_dict["bullet_reflect_amount"] = bullet_reflect_amount
        if bullet_reflect_scale is not UNSET:
            field_dict["bullet_reflect_scale"] = bullet_reflect_scale
        if bullet_whiz_distance is not UNSET:
            field_dict["bullet_whiz_distance"] = bullet_whiz_distance
        if burst_shot_cooldown is not UNSET:
            field_dict["burst_shot_cooldown"] = burst_shot_cooldown
        if crit_bonus_against_npcs is not UNSET:
            field_dict["crit_bonus_against_npcs"] = crit_bonus_against_npcs
        if crit_bonus_end is not UNSET:
            field_dict["crit_bonus_end"] = crit_bonus_end
        if crit_bonus_end_range is not UNSET:
            field_dict["crit_bonus_end_range"] = crit_bonus_end_range
        if crit_bonus_start is not UNSET:
            field_dict["crit_bonus_start"] = crit_bonus_start
        if crit_bonus_start_range is not UNSET:
            field_dict["crit_bonus_start_range"] = crit_bonus_start_range
        if cycle_time is not UNSET:
            field_dict["cycle_time"] = cycle_time
        if intra_burst_cycle_time is not UNSET:
            field_dict["intra_burst_cycle_time"] = intra_burst_cycle_time
        if max_spin_cycle_time is not UNSET:
            field_dict["max_spin_cycle_time"] = max_spin_cycle_time
        if damage_falloff_bias is not UNSET:
            field_dict["damage_falloff_bias"] = damage_falloff_bias
        if damage_falloff_end_range is not UNSET:
            field_dict["damage_falloff_end_range"] = damage_falloff_end_range
        if damage_falloff_end_scale is not UNSET:
            field_dict["damage_falloff_end_scale"] = damage_falloff_end_scale
        if damage_falloff_start_range is not UNSET:
            field_dict["damage_falloff_start_range"] = damage_falloff_start_range
        if damage_falloff_start_scale is not UNSET:
            field_dict["damage_falloff_start_scale"] = damage_falloff_start_scale
        if horizontal_punch is not UNSET:
            field_dict["horizontal_punch"] = horizontal_punch
        if range_ is not UNSET:
            field_dict["range"] = range_
        if recoil_recovery_delay_factor is not UNSET:
            field_dict["recoil_recovery_delay_factor"] = recoil_recovery_delay_factor
        if recoil_recovery_speed is not UNSET:
            field_dict["recoil_recovery_speed"] = recoil_recovery_speed
        if recoil_shot_index_recovery_time_factor is not UNSET:
            field_dict["recoil_shot_index_recovery_time_factor"] = recoil_shot_index_recovery_time_factor
        if recoil_speed is not UNSET:
            field_dict["recoil_speed"] = recoil_speed
        if reload_move_speed is not UNSET:
            field_dict["reload_move_speed"] = reload_move_speed
        if scatter_yaw_scale is not UNSET:
            field_dict["scatter_yaw_scale"] = scatter_yaw_scale
        if aiming_shot_spread_penalty is not UNSET:
            field_dict["aiming_shot_spread_penalty"] = aiming_shot_spread_penalty
        if standing_shot_spread_penalty is not UNSET:
            field_dict["standing_shot_spread_penalty"] = standing_shot_spread_penalty
        if shoot_move_speed_percent is not UNSET:
            field_dict["shoot_move_speed_percent"] = shoot_move_speed_percent
        if shoot_spread_penalty_decay is not UNSET:
            field_dict["shoot_spread_penalty_decay"] = shoot_spread_penalty_decay
        if shoot_spread_penalty_decay_delay is not UNSET:
            field_dict["shoot_spread_penalty_decay_delay"] = shoot_spread_penalty_decay_delay
        if shoot_spread_penalty_per_shot is not UNSET:
            field_dict["shoot_spread_penalty_per_shot"] = shoot_spread_penalty_per_shot
        if shooting_up_spread_penalty is not UNSET:
            field_dict["shooting_up_spread_penalty"] = shooting_up_spread_penalty
        if vertical_punch is not UNSET:
            field_dict["vertical_punch"] = vertical_punch
        if zoom_fov is not UNSET:
            field_dict["zoom_fov"] = zoom_fov
        if zoom_move_speed_percent is not UNSET:
            field_dict["zoom_move_speed_percent"] = zoom_move_speed_percent
        if bullets is not UNSET:
            field_dict["bullets"] = bullets
        if burst_shot_count is not UNSET:
            field_dict["burst_shot_count"] = burst_shot_count
        if clip_size is not UNSET:
            field_dict["clip_size"] = clip_size
        if spread is not UNSET:
            field_dict["spread"] = spread
        if standing_spread is not UNSET:
            field_dict["standing_spread"] = standing_spread
        if low_ammo_indicator_threshold is not UNSET:
            field_dict["low_ammo_indicator_threshold"] = low_ammo_indicator_threshold
        if recoil_seed is not UNSET:
            field_dict["recoil_seed"] = recoil_seed
        if reload_duration is not UNSET:
            field_dict["reload_duration"] = reload_duration
        if bullet_speed_curve is not UNSET:
            field_dict["bullet_speed_curve"] = bullet_speed_curve
        if horizontal_recoil is not UNSET:
            field_dict["horizontal_recoil"] = horizontal_recoil
        if vertical_recoil is not UNSET:
            field_dict["vertical_recoil"] = vertical_recoil

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_item_weapon_info_bullet_speed_curve_v2 import RawItemWeaponInfoBulletSpeedCurveV2
        from ..models.raw_weapon_info_horizontal_recoil_v2 import RawWeaponInfoHorizontalRecoilV2
        from ..models.raw_weapon_info_vertical_recoil_v2 import RawWeaponInfoVerticalRecoilV2

        d = dict(src_dict)

        def _parse_can_zoom(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        can_zoom = _parse_can_zoom(d.pop("can_zoom", UNSET))

        def _parse_bullet_damage(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bullet_damage = _parse_bullet_damage(d.pop("bullet_damage", UNSET))

        def _parse_bullet_gravity_scale(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bullet_gravity_scale = _parse_bullet_gravity_scale(d.pop("bullet_gravity_scale", UNSET))

        def _parse_bullet_inherit_shooter_velocity_scale(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bullet_inherit_shooter_velocity_scale = _parse_bullet_inherit_shooter_velocity_scale(
            d.pop("bullet_inherit_shooter_velocity_scale", UNSET)
        )

        def _parse_bullet_lifetime(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bullet_lifetime = _parse_bullet_lifetime(d.pop("bullet_lifetime", UNSET))

        def _parse_bullet_radius(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bullet_radius = _parse_bullet_radius(d.pop("bullet_radius", UNSET))

        def _parse_bullet_radius_vs_world(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bullet_radius_vs_world = _parse_bullet_radius_vs_world(d.pop("bullet_radius_vs_world", UNSET))

        def _parse_bullet_reflect_amount(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bullet_reflect_amount = _parse_bullet_reflect_amount(d.pop("bullet_reflect_amount", UNSET))

        def _parse_bullet_reflect_scale(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bullet_reflect_scale = _parse_bullet_reflect_scale(d.pop("bullet_reflect_scale", UNSET))

        def _parse_bullet_whiz_distance(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bullet_whiz_distance = _parse_bullet_whiz_distance(d.pop("bullet_whiz_distance", UNSET))

        def _parse_burst_shot_cooldown(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        burst_shot_cooldown = _parse_burst_shot_cooldown(d.pop("burst_shot_cooldown", UNSET))

        def _parse_crit_bonus_against_npcs(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crit_bonus_against_npcs = _parse_crit_bonus_against_npcs(d.pop("crit_bonus_against_npcs", UNSET))

        def _parse_crit_bonus_end(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crit_bonus_end = _parse_crit_bonus_end(d.pop("crit_bonus_end", UNSET))

        def _parse_crit_bonus_end_range(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crit_bonus_end_range = _parse_crit_bonus_end_range(d.pop("crit_bonus_end_range", UNSET))

        def _parse_crit_bonus_start(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crit_bonus_start = _parse_crit_bonus_start(d.pop("crit_bonus_start", UNSET))

        def _parse_crit_bonus_start_range(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crit_bonus_start_range = _parse_crit_bonus_start_range(d.pop("crit_bonus_start_range", UNSET))

        def _parse_cycle_time(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cycle_time = _parse_cycle_time(d.pop("cycle_time", UNSET))

        def _parse_intra_burst_cycle_time(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        intra_burst_cycle_time = _parse_intra_burst_cycle_time(d.pop("intra_burst_cycle_time", UNSET))

        def _parse_max_spin_cycle_time(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_spin_cycle_time = _parse_max_spin_cycle_time(d.pop("max_spin_cycle_time", UNSET))

        def _parse_damage_falloff_bias(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        damage_falloff_bias = _parse_damage_falloff_bias(d.pop("damage_falloff_bias", UNSET))

        def _parse_damage_falloff_end_range(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        damage_falloff_end_range = _parse_damage_falloff_end_range(d.pop("damage_falloff_end_range", UNSET))

        def _parse_damage_falloff_end_scale(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        damage_falloff_end_scale = _parse_damage_falloff_end_scale(d.pop("damage_falloff_end_scale", UNSET))

        def _parse_damage_falloff_start_range(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        damage_falloff_start_range = _parse_damage_falloff_start_range(d.pop("damage_falloff_start_range", UNSET))

        def _parse_damage_falloff_start_scale(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        damage_falloff_start_scale = _parse_damage_falloff_start_scale(d.pop("damage_falloff_start_scale", UNSET))

        def _parse_horizontal_punch(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        horizontal_punch = _parse_horizontal_punch(d.pop("horizontal_punch", UNSET))

        def _parse_range_(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        range_ = _parse_range_(d.pop("range", UNSET))

        def _parse_recoil_recovery_delay_factor(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        recoil_recovery_delay_factor = _parse_recoil_recovery_delay_factor(d.pop("recoil_recovery_delay_factor", UNSET))

        def _parse_recoil_recovery_speed(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        recoil_recovery_speed = _parse_recoil_recovery_speed(d.pop("recoil_recovery_speed", UNSET))

        def _parse_recoil_shot_index_recovery_time_factor(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        recoil_shot_index_recovery_time_factor = _parse_recoil_shot_index_recovery_time_factor(
            d.pop("recoil_shot_index_recovery_time_factor", UNSET)
        )

        def _parse_recoil_speed(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        recoil_speed = _parse_recoil_speed(d.pop("recoil_speed", UNSET))

        def _parse_reload_move_speed(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        reload_move_speed = _parse_reload_move_speed(d.pop("reload_move_speed", UNSET))

        def _parse_scatter_yaw_scale(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        scatter_yaw_scale = _parse_scatter_yaw_scale(d.pop("scatter_yaw_scale", UNSET))

        def _parse_aiming_shot_spread_penalty(data: object) -> Union[None, Unset, list[float], str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aiming_shot_spread_penalty_type_0 = cast(list[float], data)

                return aiming_shot_spread_penalty_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[float], str], data)

        aiming_shot_spread_penalty = _parse_aiming_shot_spread_penalty(d.pop("aiming_shot_spread_penalty", UNSET))

        def _parse_standing_shot_spread_penalty(data: object) -> Union[None, Unset, list[float], str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                standing_shot_spread_penalty_type_0 = cast(list[float], data)

                return standing_shot_spread_penalty_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[float], str], data)

        standing_shot_spread_penalty = _parse_standing_shot_spread_penalty(d.pop("standing_shot_spread_penalty", UNSET))

        def _parse_shoot_move_speed_percent(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shoot_move_speed_percent = _parse_shoot_move_speed_percent(d.pop("shoot_move_speed_percent", UNSET))

        def _parse_shoot_spread_penalty_decay(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shoot_spread_penalty_decay = _parse_shoot_spread_penalty_decay(d.pop("shoot_spread_penalty_decay", UNSET))

        def _parse_shoot_spread_penalty_decay_delay(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shoot_spread_penalty_decay_delay = _parse_shoot_spread_penalty_decay_delay(
            d.pop("shoot_spread_penalty_decay_delay", UNSET)
        )

        def _parse_shoot_spread_penalty_per_shot(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shoot_spread_penalty_per_shot = _parse_shoot_spread_penalty_per_shot(
            d.pop("shoot_spread_penalty_per_shot", UNSET)
        )

        def _parse_shooting_up_spread_penalty(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shooting_up_spread_penalty = _parse_shooting_up_spread_penalty(d.pop("shooting_up_spread_penalty", UNSET))

        def _parse_vertical_punch(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        vertical_punch = _parse_vertical_punch(d.pop("vertical_punch", UNSET))

        def _parse_zoom_fov(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        zoom_fov = _parse_zoom_fov(d.pop("zoom_fov", UNSET))

        def _parse_zoom_move_speed_percent(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        zoom_move_speed_percent = _parse_zoom_move_speed_percent(d.pop("zoom_move_speed_percent", UNSET))

        def _parse_bullets(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bullets = _parse_bullets(d.pop("bullets", UNSET))

        def _parse_burst_shot_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        burst_shot_count = _parse_burst_shot_count(d.pop("burst_shot_count", UNSET))

        def _parse_clip_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        clip_size = _parse_clip_size(d.pop("clip_size", UNSET))

        def _parse_spread(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        spread = _parse_spread(d.pop("spread", UNSET))

        def _parse_standing_spread(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        standing_spread = _parse_standing_spread(d.pop("standing_spread", UNSET))

        def _parse_low_ammo_indicator_threshold(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        low_ammo_indicator_threshold = _parse_low_ammo_indicator_threshold(d.pop("low_ammo_indicator_threshold", UNSET))

        def _parse_recoil_seed(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        recoil_seed = _parse_recoil_seed(d.pop("recoil_seed", UNSET))

        def _parse_reload_duration(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        reload_duration = _parse_reload_duration(d.pop("reload_duration", UNSET))

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

        def _parse_horizontal_recoil(data: object) -> Union["RawWeaponInfoHorizontalRecoilV2", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                horizontal_recoil_type_0 = RawWeaponInfoHorizontalRecoilV2.from_dict(data)

                return horizontal_recoil_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RawWeaponInfoHorizontalRecoilV2", None, Unset], data)

        horizontal_recoil = _parse_horizontal_recoil(d.pop("horizontal_recoil", UNSET))

        def _parse_vertical_recoil(data: object) -> Union["RawWeaponInfoVerticalRecoilV2", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vertical_recoil_type_0 = RawWeaponInfoVerticalRecoilV2.from_dict(data)

                return vertical_recoil_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RawWeaponInfoVerticalRecoilV2", None, Unset], data)

        vertical_recoil = _parse_vertical_recoil(d.pop("vertical_recoil", UNSET))

        raw_weapon_info_v2 = cls(
            can_zoom=can_zoom,
            bullet_damage=bullet_damage,
            bullet_gravity_scale=bullet_gravity_scale,
            bullet_inherit_shooter_velocity_scale=bullet_inherit_shooter_velocity_scale,
            bullet_lifetime=bullet_lifetime,
            bullet_radius=bullet_radius,
            bullet_radius_vs_world=bullet_radius_vs_world,
            bullet_reflect_amount=bullet_reflect_amount,
            bullet_reflect_scale=bullet_reflect_scale,
            bullet_whiz_distance=bullet_whiz_distance,
            burst_shot_cooldown=burst_shot_cooldown,
            crit_bonus_against_npcs=crit_bonus_against_npcs,
            crit_bonus_end=crit_bonus_end,
            crit_bonus_end_range=crit_bonus_end_range,
            crit_bonus_start=crit_bonus_start,
            crit_bonus_start_range=crit_bonus_start_range,
            cycle_time=cycle_time,
            intra_burst_cycle_time=intra_burst_cycle_time,
            max_spin_cycle_time=max_spin_cycle_time,
            damage_falloff_bias=damage_falloff_bias,
            damage_falloff_end_range=damage_falloff_end_range,
            damage_falloff_end_scale=damage_falloff_end_scale,
            damage_falloff_start_range=damage_falloff_start_range,
            damage_falloff_start_scale=damage_falloff_start_scale,
            horizontal_punch=horizontal_punch,
            range_=range_,
            recoil_recovery_delay_factor=recoil_recovery_delay_factor,
            recoil_recovery_speed=recoil_recovery_speed,
            recoil_shot_index_recovery_time_factor=recoil_shot_index_recovery_time_factor,
            recoil_speed=recoil_speed,
            reload_move_speed=reload_move_speed,
            scatter_yaw_scale=scatter_yaw_scale,
            aiming_shot_spread_penalty=aiming_shot_spread_penalty,
            standing_shot_spread_penalty=standing_shot_spread_penalty,
            shoot_move_speed_percent=shoot_move_speed_percent,
            shoot_spread_penalty_decay=shoot_spread_penalty_decay,
            shoot_spread_penalty_decay_delay=shoot_spread_penalty_decay_delay,
            shoot_spread_penalty_per_shot=shoot_spread_penalty_per_shot,
            shooting_up_spread_penalty=shooting_up_spread_penalty,
            vertical_punch=vertical_punch,
            zoom_fov=zoom_fov,
            zoom_move_speed_percent=zoom_move_speed_percent,
            bullets=bullets,
            burst_shot_count=burst_shot_count,
            clip_size=clip_size,
            spread=spread,
            standing_spread=standing_spread,
            low_ammo_indicator_threshold=low_ammo_indicator_threshold,
            recoil_seed=recoil_seed,
            reload_duration=reload_duration,
            bullet_speed_curve=bullet_speed_curve,
            horizontal_recoil=horizontal_recoil,
            vertical_recoil=vertical_recoil,
        )

        raw_weapon_info_v2.additional_properties = d
        return raw_weapon_info_v2

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
