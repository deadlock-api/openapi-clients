# WeaponInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aiming_shot_spread_penalty** | **object** |  | [optional] 
**build_up_rate** | **float** |  | [optional] 
**bullet_damage** | **float** |  | [optional] 
**bullet_gravity_scale** | **float** |  | [optional] 
**bullet_inherit_shooter_velocity_scale** | **float** |  | [optional] 
**bullet_lifetime** | **float** |  | [optional] 
**bullet_radius** | **float** |  | [optional] 
**bullet_radius_vs_world** | **float** |  | [optional] 
**bullet_reflect_amount** | **float** |  | [optional] 
**bullet_reflect_scale** | **float** |  | [optional] 
**bullet_speed** | **float** |  | [optional] 
**bullet_speed_curve** | [**RawItemWeaponInfoBulletSpeedCurve**](RawItemWeaponInfoBulletSpeedCurve.md) |  | [optional] 
**bullet_whiz_distance** | **float** |  | [optional] 
**bullets** | **int** |  | [optional] 
**bullets_per_second** | **float** |  | [optional] 
**bullets_per_second_with_reload** | **float** |  | [optional] 
**burst_shot_cooldown** | **float** |  | [optional] 
**burst_shot_count** | **int** |  | [optional] 
**can_zoom** | **bool** |  | [optional] 
**clip_size** | **int** |  | [optional] 
**crit_bonus_against_npcs** | **float** |  | [optional] 
**crit_bonus_end** | **float** |  | [optional] 
**crit_bonus_end_range** | **float** |  | [optional] 
**crit_bonus_start** | **float** |  | [optional] 
**crit_bonus_start_range** | **float** |  | [optional] 
**cycle_time** | **float** |  | [optional] 
**damage_falloff_bias** | **float** |  | [optional] 
**damage_falloff_end_range** | **float** |  | [optional] 
**damage_falloff_end_scale** | **float** |  | [optional] 
**damage_falloff_start_range** | **float** |  | [optional] 
**damage_falloff_start_scale** | **float** |  | [optional] 
**damage_per_magazine** | **float** |  | [optional] 
**damage_per_second** | **float** |  | [optional] 
**damage_per_second_with_reload** | **float** |  | [optional] 
**damage_per_shot** | **float** |  | [optional] 
**horizontal_punch** | **float** |  | [optional] 
**horizontal_recoil** | [**RawWeaponInfoHorizontalRecoil**](RawWeaponInfoHorizontalRecoil.md) |  | [optional] 
**intra_burst_cycle_time** | **float** |  | [optional] 
**is_semi_auto** | **bool** |  | [optional] 
**low_ammo_indicator_threshold** | **float** |  | [optional] 
**max_spin_cycle_time** | **float** |  | [optional] 
**range** | **float** |  | [optional] 
**recoil_recovery_delay_factor** | **float** |  | [optional] 
**recoil_recovery_speed** | **float** |  | [optional] 
**recoil_seed** | **float** |  | [optional] 
**recoil_shot_index_recovery_time_factor** | **float** |  | [optional] 
**recoil_speed** | **float** |  | [optional] 
**reload_duration** | **float** |  | [optional] 
**reload_move_speed** | **float** |  | [optional] 
**reload_single_bullets** | **bool** |  | [optional] 
**reload_single_bullets_allow_cancel** | **bool** |  | [optional] 
**reload_single_bullets_initial_delay** | **float** |  | [optional] 
**scatter_yaw_scale** | **float** |  | [optional] 
**semi_auto_cycle_rate** | **float** |  | [optional] 
**shoot_move_speed_percent** | **float** |  | [optional] 
**shoot_spread_penalty_decay** | **float** |  | [optional] 
**shoot_spread_penalty_decay_delay** | **float** |  | [optional] 
**shoot_spread_penalty_per_shot** | **float** |  | [optional] 
**shooting_up_spread_penalty** | **float** |  | [optional] 
**shots_per_second** | **float** |  | [optional] 
**shots_per_second_with_reload** | **float** |  | [optional] 
**spin_decay_rate** | **float** |  | [optional] 
**spin_increase_rate** | **float** |  | [optional] 
**spins_up** | **bool** |  | [optional] 
**spread** | **float** |  | [optional] 
**standing_shot_spread_penalty** | **object** |  | [optional] 
**standing_spread** | **float** |  | [optional] 
**vertical_punch** | **float** |  | [optional] 
**vertical_recoil** | [**RawWeaponInfoVerticalRecoil**](RawWeaponInfoVerticalRecoil.md) |  | [optional] 
**zoom_fov** | **float** |  | [optional] 
**zoom_move_speed_percent** | **float** |  | [optional] 

## Example

```python
from deadlock_api_client.models.weapon_info import WeaponInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WeaponInfo from a JSON string
weapon_info_instance = WeaponInfo.from_json(json)
# print the JSON string representation of the object
print(WeaponInfo.to_json())

# convert the object into a dict
weapon_info_dict = weapon_info_instance.to_dict()
# create an instance of WeaponInfo from a dict
weapon_info_from_dict = WeaponInfo.from_dict(weapon_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


