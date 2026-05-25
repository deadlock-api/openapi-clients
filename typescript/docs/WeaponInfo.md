# WeaponInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aiming_shot_spread_penalty** | **any** |  | [optional] [default to undefined]
**build_up_rate** | **number** |  | [optional] [default to undefined]
**bullet_damage** | **number** |  | [optional] [default to undefined]
**bullet_gravity_scale** | **number** |  | [optional] [default to undefined]
**bullet_inherit_shooter_velocity_scale** | **number** |  | [optional] [default to undefined]
**bullet_lifetime** | **number** |  | [optional] [default to undefined]
**bullet_radius** | **number** |  | [optional] [default to undefined]
**bullet_radius_vs_world** | **number** |  | [optional] [default to undefined]
**bullet_reflect_amount** | **number** |  | [optional] [default to undefined]
**bullet_reflect_scale** | **number** |  | [optional] [default to undefined]
**bullet_speed** | **number** |  | [optional] [default to undefined]
**bullet_speed_curve** | [**RawItemWeaponInfoBulletSpeedCurve**](RawItemWeaponInfoBulletSpeedCurve.md) |  | [optional] [default to undefined]
**bullet_whiz_distance** | **number** |  | [optional] [default to undefined]
**bullets** | **number** |  | [optional] [default to undefined]
**bullets_per_second** | **number** |  | [optional] [default to undefined]
**bullets_per_second_with_reload** | **number** |  | [optional] [default to undefined]
**burst_shot_cooldown** | **number** |  | [optional] [default to undefined]
**burst_shot_count** | **number** |  | [optional] [default to undefined]
**can_zoom** | **boolean** |  | [optional] [default to undefined]
**clip_size** | **number** |  | [optional] [default to undefined]
**crit_bonus_against_npcs** | **number** |  | [optional] [default to undefined]
**crit_bonus_end** | **number** |  | [optional] [default to undefined]
**crit_bonus_end_range** | **number** |  | [optional] [default to undefined]
**crit_bonus_start** | **number** |  | [optional] [default to undefined]
**crit_bonus_start_range** | **number** |  | [optional] [default to undefined]
**cycle_time** | **number** |  | [optional] [default to undefined]
**damage_falloff_bias** | **number** |  | [optional] [default to undefined]
**damage_falloff_end_range** | **number** |  | [optional] [default to undefined]
**damage_falloff_end_scale** | **number** |  | [optional] [default to undefined]
**damage_falloff_start_range** | **number** |  | [optional] [default to undefined]
**damage_falloff_start_scale** | **number** |  | [optional] [default to undefined]
**damage_per_magazine** | **number** |  | [optional] [default to undefined]
**damage_per_second** | **number** |  | [optional] [default to undefined]
**damage_per_second_with_reload** | **number** |  | [optional] [default to undefined]
**damage_per_shot** | **number** |  | [optional] [default to undefined]
**horizontal_punch** | **number** |  | [optional] [default to undefined]
**horizontal_recoil** | [**RawWeaponInfoHorizontalRecoil**](RawWeaponInfoHorizontalRecoil.md) |  | [optional] [default to undefined]
**intra_burst_cycle_time** | **number** |  | [optional] [default to undefined]
**is_semi_auto** | **boolean** |  | [optional] [default to undefined]
**low_ammo_indicator_threshold** | **number** |  | [optional] [default to undefined]
**max_spin_cycle_time** | **number** |  | [optional] [default to undefined]
**range** | **number** |  | [optional] [default to undefined]
**recoil_recovery_delay_factor** | **number** |  | [optional] [default to undefined]
**recoil_recovery_speed** | **number** |  | [optional] [default to undefined]
**recoil_seed** | **number** |  | [optional] [default to undefined]
**recoil_shot_index_recovery_time_factor** | **number** |  | [optional] [default to undefined]
**recoil_speed** | **number** |  | [optional] [default to undefined]
**reload_duration** | **number** |  | [optional] [default to undefined]
**reload_move_speed** | **number** |  | [optional] [default to undefined]
**reload_single_bullets** | **boolean** |  | [optional] [default to undefined]
**reload_single_bullets_allow_cancel** | **boolean** |  | [optional] [default to undefined]
**reload_single_bullets_initial_delay** | **number** |  | [optional] [default to undefined]
**scatter_yaw_scale** | **number** |  | [optional] [default to undefined]
**semi_auto_cycle_rate** | **number** |  | [optional] [default to undefined]
**shoot_move_speed_percent** | **number** |  | [optional] [default to undefined]
**shoot_spread_penalty_decay** | **number** |  | [optional] [default to undefined]
**shoot_spread_penalty_decay_delay** | **number** |  | [optional] [default to undefined]
**shoot_spread_penalty_per_shot** | **number** |  | [optional] [default to undefined]
**shooting_up_spread_penalty** | **number** |  | [optional] [default to undefined]
**shots_per_second** | **number** |  | [optional] [default to undefined]
**shots_per_second_with_reload** | **number** |  | [optional] [default to undefined]
**spin_decay_rate** | **number** |  | [optional] [default to undefined]
**spin_increase_rate** | **number** |  | [optional] [default to undefined]
**spins_up** | **boolean** |  | [optional] [default to undefined]
**spread** | **number** |  | [optional] [default to undefined]
**standing_shot_spread_penalty** | **any** |  | [optional] [default to undefined]
**standing_spread** | **number** |  | [optional] [default to undefined]
**vertical_punch** | **number** |  | [optional] [default to undefined]
**vertical_recoil** | [**RawWeaponInfoVerticalRecoil**](RawWeaponInfoVerticalRecoil.md) |  | [optional] [default to undefined]
**zoom_fov** | **number** |  | [optional] [default to undefined]
**zoom_move_speed_percent** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { WeaponInfo } from 'deadlock_api_client';

const instance: WeaponInfo = {
    aiming_shot_spread_penalty,
    build_up_rate,
    bullet_damage,
    bullet_gravity_scale,
    bullet_inherit_shooter_velocity_scale,
    bullet_lifetime,
    bullet_radius,
    bullet_radius_vs_world,
    bullet_reflect_amount,
    bullet_reflect_scale,
    bullet_speed,
    bullet_speed_curve,
    bullet_whiz_distance,
    bullets,
    bullets_per_second,
    bullets_per_second_with_reload,
    burst_shot_cooldown,
    burst_shot_count,
    can_zoom,
    clip_size,
    crit_bonus_against_npcs,
    crit_bonus_end,
    crit_bonus_end_range,
    crit_bonus_start,
    crit_bonus_start_range,
    cycle_time,
    damage_falloff_bias,
    damage_falloff_end_range,
    damage_falloff_end_scale,
    damage_falloff_start_range,
    damage_falloff_start_scale,
    damage_per_magazine,
    damage_per_second,
    damage_per_second_with_reload,
    damage_per_shot,
    horizontal_punch,
    horizontal_recoil,
    intra_burst_cycle_time,
    is_semi_auto,
    low_ammo_indicator_threshold,
    max_spin_cycle_time,
    range,
    recoil_recovery_delay_factor,
    recoil_recovery_speed,
    recoil_seed,
    recoil_shot_index_recovery_time_factor,
    recoil_speed,
    reload_duration,
    reload_move_speed,
    reload_single_bullets,
    reload_single_bullets_allow_cancel,
    reload_single_bullets_initial_delay,
    scatter_yaw_scale,
    semi_auto_cycle_rate,
    shoot_move_speed_percent,
    shoot_spread_penalty_decay,
    shoot_spread_penalty_decay_delay,
    shoot_spread_penalty_per_shot,
    shooting_up_spread_penalty,
    shots_per_second,
    shots_per_second_with_reload,
    spin_decay_rate,
    spin_increase_rate,
    spins_up,
    spread,
    standing_shot_spread_penalty,
    standing_spread,
    vertical_punch,
    vertical_recoil,
    zoom_fov,
    zoom_move_speed_percent,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
