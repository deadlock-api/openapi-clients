# WeaponInfoV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_zoom** | **bool** |  | [optional] 
**bullet_damage** | **float** |  | [optional] 
**bullet_gravity_scale** | **float** |  | [optional] 
**bullet_inherit_shooter_velocity_scale** | **float** |  | [optional] 
**bullet_lifetime** | **float** |  | [optional] 
**bullet_radius** | **float** |  | [optional] 
**bullet_radius_vs_world** | **float** |  | [optional] 
**bullet_reflect_amount** | **float** |  | [optional] 
**bullet_reflect_scale** | **float** |  | [optional] 
**bullet_whiz_distance** | **float** |  | [optional] 
**burst_shot_cooldown** | **float** |  | [optional] 
**crit_bonus_against_npcs** | **float** |  | [optional] 
**crit_bonus_end** | **float** |  | [optional] 
**crit_bonus_end_range** | **float** |  | [optional] 
**crit_bonus_start** | **float** |  | [optional] 
**crit_bonus_start_range** | **float** |  | [optional] 
**cycle_time** | **float** |  | [optional] 
**spins_up** | **bool** |  | [optional] 
**is_semi_auto** | **bool** |  | [optional] 
**semi_auto_cycle_rate** | **float** |  | [optional] 
**max_spin_cycle_time** | **float** |  | [optional] 
**spin_increase_rate** | **float** |  | [optional] 
**spin_decay_rate** | **float** |  | [optional] 
**build_up_rate** | **float** |  | [optional] 
**intra_burst_cycle_time** | **float** |  | [optional] 
**damage_falloff_bias** | **float** |  | [optional] 
**damage_falloff_end_range** | **float** |  | [optional] 
**damage_falloff_end_scale** | **float** |  | [optional] 
**damage_falloff_start_range** | **float** |  | [optional] 
**damage_falloff_start_scale** | **float** |  | [optional] 
**horizontal_punch** | **float** |  | [optional] 
**range** | **float** |  | [optional] 
**recoil_recovery_delay_factor** | **float** |  | [optional] 
**bullet_speed** | **float** |  | [optional] 
**recoil_recovery_speed** | **float** |  | [optional] 
**recoil_shot_index_recovery_time_factor** | **float** |  | [optional] 
**recoil_speed** | **float** |  | [optional] 
**reload_move_speed** | **float** |  | [optional] 
**scatter_yaw_scale** | **float** |  | [optional] 
**aiming_shot_spread_penalty** | [**AimingShotSpreadPenalty**](AimingShotSpreadPenalty.md) |  | [optional] 
**standing_shot_spread_penalty** | [**StandingShotSpreadPenalty**](StandingShotSpreadPenalty.md) |  | [optional] 
**shoot_move_speed_percent** | **float** |  | [optional] 
**shoot_spread_penalty_decay** | **float** |  | [optional] 
**shoot_spread_penalty_decay_delay** | **float** |  | [optional] 
**shoot_spread_penalty_per_shot** | **float** |  | [optional] 
**shooting_up_spread_penalty** | **float** |  | [optional] 
**vertical_punch** | **float** |  | [optional] 
**zoom_fov** | **float** |  | [optional] 
**zoom_move_speed_percent** | **float** |  | [optional] 
**bullets** | **int** |  | [optional] 
**reload_single_bullets_initial_delay** | **float** |  | [optional] 
**reload_single_bullets** | **bool** |  | [optional] 
**reload_single_bullets_allow_cancel** | **bool** |  | [optional] 
**burst_shot_count** | **int** |  | [optional] 
**clip_size** | **int** |  | [optional] 
**spread** | **float** |  | [optional] 
**standing_spread** | **float** |  | [optional] 
**low_ammo_indicator_threshold** | **float** |  | [optional] 
**recoil_seed** | **float** |  | [optional] 
**reload_duration** | **float** |  | [optional] 
**bullet_speed_curve** | [**RawItemWeaponInfoBulletSpeedCurveV2**](RawItemWeaponInfoBulletSpeedCurveV2.md) |  | [optional] 
**horizontal_recoil** | [**RawWeaponInfoHorizontalRecoilV2**](RawWeaponInfoHorizontalRecoilV2.md) |  | [optional] 
**vertical_recoil** | [**RawWeaponInfoVerticalRecoilV2**](RawWeaponInfoVerticalRecoilV2.md) |  | [optional] 
**shots_per_second** | **float** |  | [readonly] 
**shots_per_second_with_reload** | **float** |  | [readonly] 
**bullets_per_second** | **float** |  | [readonly] 
**bullets_per_second_with_reload** | **float** |  | [readonly] 
**damage_per_second** | **float** |  | [readonly] 
**damage_per_second_with_reload** | **float** |  | [readonly] 
**damage_per_shot** | **float** |  | [readonly] 
**damage_per_magazine** | **float** |  | [readonly] 

## Example

```python
from assets_deadlock_api_client.models.weapon_info_v2 import WeaponInfoV2

# TODO update the JSON string below
json = "{}"
# create an instance of WeaponInfoV2 from a JSON string
weapon_info_v2_instance = WeaponInfoV2.from_json(json)
# print the JSON string representation of the object
print(WeaponInfoV2.to_json())

# convert the object into a dict
weapon_info_v2_dict = weapon_info_v2_instance.to_dict()
# create an instance of WeaponInfoV2 from a dict
weapon_info_v2_from_dict = WeaponInfoV2.from_dict(weapon_info_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


