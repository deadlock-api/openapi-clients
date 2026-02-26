# RawWeaponInfoV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_zoom** | **boolean** |  | [optional] [default to undefined]
**bullet_damage** | **number** |  | [optional] [default to undefined]
**bullet_gravity_scale** | **number** |  | [optional] [default to undefined]
**bullet_inherit_shooter_velocity_scale** | **number** |  | [optional] [default to undefined]
**bullet_lifetime** | **number** |  | [optional] [default to undefined]
**bullet_radius** | **number** |  | [optional] [default to undefined]
**bullet_radius_vs_world** | **number** |  | [optional] [default to undefined]
**bullet_reflect_amount** | **number** |  | [optional] [default to undefined]
**bullet_reflect_scale** | **number** |  | [optional] [default to undefined]
**bullet_whiz_distance** | **number** |  | [optional] [default to undefined]
**burst_shot_cooldown** | **number** |  | [optional] [default to undefined]
**crit_bonus_against_npcs** | **number** |  | [optional] [default to undefined]
**crit_bonus_end** | **number** |  | [optional] [default to undefined]
**crit_bonus_end_range** | **number** |  | [optional] [default to undefined]
**crit_bonus_start** | **number** |  | [optional] [default to undefined]
**crit_bonus_start_range** | **number** |  | [optional] [default to undefined]
**cycle_time** | **number** |  | [optional] [default to undefined]
**spins_up** | **boolean** |  | [optional] [default to undefined]
**is_semi_auto** | **boolean** |  | [optional] [default to undefined]
**semi_auto_cycle_rate** | **number** |  | [optional] [default to undefined]
**max_spin_cycle_time** | **number** |  | [optional] [default to undefined]
**spin_increase_rate** | **number** |  | [optional] [default to undefined]
**spin_decay_rate** | **number** |  | [optional] [default to undefined]
**build_up_rate** | **number** |  | [optional] [default to undefined]
**intra_burst_cycle_time** | **number** |  | [optional] [default to undefined]
**damage_falloff_bias** | **number** |  | [optional] [default to undefined]
**damage_falloff_end_range** | **number** |  | [optional] [default to undefined]
**damage_falloff_end_scale** | **number** |  | [optional] [default to undefined]
**damage_falloff_start_range** | **number** |  | [optional] [default to undefined]
**damage_falloff_start_scale** | **number** |  | [optional] [default to undefined]
**horizontal_punch** | **number** |  | [optional] [default to undefined]
**range** | **number** |  | [optional] [default to undefined]
**recoil_recovery_delay_factor** | **number** |  | [optional] [default to undefined]
**bullet_speed** | **number** |  | [optional] [default to undefined]
**recoil_recovery_speed** | **number** |  | [optional] [default to undefined]
**recoil_shot_index_recovery_time_factor** | **number** |  | [optional] [default to undefined]
**recoil_speed** | **number** |  | [optional] [default to undefined]
**reload_move_speed** | **number** |  | [optional] [default to undefined]
**scatter_yaw_scale** | **number** |  | [optional] [default to undefined]
**aiming_shot_spread_penalty** | [**AimingShotSpreadPenalty**](AimingShotSpreadPenalty.md) |  | [optional] [default to undefined]
**standing_shot_spread_penalty** | [**StandingShotSpreadPenalty**](StandingShotSpreadPenalty.md) |  | [optional] [default to undefined]
**shoot_move_speed_percent** | **number** |  | [optional] [default to undefined]
**shoot_spread_penalty_decay** | **number** |  | [optional] [default to undefined]
**shoot_spread_penalty_decay_delay** | **number** |  | [optional] [default to undefined]
**shoot_spread_penalty_per_shot** | **number** |  | [optional] [default to undefined]
**shooting_up_spread_penalty** | **number** |  | [optional] [default to undefined]
**vertical_punch** | **number** |  | [optional] [default to undefined]
**zoom_fov** | **number** |  | [optional] [default to undefined]
**zoom_move_speed_percent** | **number** |  | [optional] [default to undefined]
**bullets** | **number** |  | [optional] [default to undefined]
**reload_single_bullets_initial_delay** | **number** |  | [optional] [default to undefined]
**reload_single_bullets** | **boolean** |  | [optional] [default to undefined]
**reload_single_bullets_allow_cancel** | **boolean** |  | [optional] [default to undefined]
**burst_shot_count** | **number** |  | [optional] [default to undefined]
**clip_size** | **number** |  | [optional] [default to undefined]
**spread** | **number** |  | [optional] [default to undefined]
**standing_spread** | **number** |  | [optional] [default to undefined]
**low_ammo_indicator_threshold** | **number** |  | [optional] [default to undefined]
**recoil_seed** | **number** |  | [optional] [default to undefined]
**reload_duration** | **number** |  | [optional] [default to undefined]
**bullet_speed_curve** | [**RawItemWeaponInfoBulletSpeedCurveV2**](RawItemWeaponInfoBulletSpeedCurveV2.md) |  | [optional] [default to undefined]
**horizontal_recoil** | [**RawWeaponInfoHorizontalRecoilV2**](RawWeaponInfoHorizontalRecoilV2.md) |  | [optional] [default to undefined]
**vertical_recoil** | [**RawWeaponInfoVerticalRecoilV2**](RawWeaponInfoVerticalRecoilV2.md) |  | [optional] [default to undefined]

## Example

```typescript
import { RawWeaponInfoV2 } from 'assets_deadlock_api_client';

const instance: RawWeaponInfoV2 = {
    can_zoom,
    bullet_damage,
    bullet_gravity_scale,
    bullet_inherit_shooter_velocity_scale,
    bullet_lifetime,
    bullet_radius,
    bullet_radius_vs_world,
    bullet_reflect_amount,
    bullet_reflect_scale,
    bullet_whiz_distance,
    burst_shot_cooldown,
    crit_bonus_against_npcs,
    crit_bonus_end,
    crit_bonus_end_range,
    crit_bonus_start,
    crit_bonus_start_range,
    cycle_time,
    spins_up,
    is_semi_auto,
    semi_auto_cycle_rate,
    max_spin_cycle_time,
    spin_increase_rate,
    spin_decay_rate,
    build_up_rate,
    intra_burst_cycle_time,
    damage_falloff_bias,
    damage_falloff_end_range,
    damage_falloff_end_scale,
    damage_falloff_start_range,
    damage_falloff_start_scale,
    horizontal_punch,
    range,
    recoil_recovery_delay_factor,
    bullet_speed,
    recoil_recovery_speed,
    recoil_shot_index_recovery_time_factor,
    recoil_speed,
    reload_move_speed,
    scatter_yaw_scale,
    aiming_shot_spread_penalty,
    standing_shot_spread_penalty,
    shoot_move_speed_percent,
    shoot_spread_penalty_decay,
    shoot_spread_penalty_decay_delay,
    shoot_spread_penalty_per_shot,
    shooting_up_spread_penalty,
    vertical_punch,
    zoom_fov,
    zoom_move_speed_percent,
    bullets,
    reload_single_bullets_initial_delay,
    reload_single_bullets,
    reload_single_bullets_allow_cancel,
    burst_shot_count,
    clip_size,
    spread,
    standing_spread,
    low_ammo_indicator_threshold,
    recoil_seed,
    reload_duration,
    bullet_speed_curve,
    horizontal_recoil,
    vertical_recoil,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
