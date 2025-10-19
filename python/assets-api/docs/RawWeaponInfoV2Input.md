# RawWeaponInfoV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_b_can_zoom** | **bool** |  | [optional] 
**m_fl_bullet_damage** | **float** |  | [optional] 
**m_fl_bullet_gravity_scale** | **float** |  | [optional] 
**m_fl_bullet_inherit_shooter_velocity_scale** | **float** |  | [optional] 
**m_fl_bullet_lifetime** | **float** |  | [optional] 
**m_fl_bullet_radius** | **float** |  | [optional] 
**m_fl_bullet_radius_vs_world** | **float** |  | [optional] 
**m_fl_bullet_reflect_amount** | **float** |  | [optional] 
**m_fl_bullet_reflect_scale** | **float** |  | [optional] 
**m_fl_bullet_whiz_distance** | **float** |  | [optional] 
**m_fl_burst_shot_cooldown** | **float** |  | [optional] 
**m_fl_crit_bonus_against_npcs** | **float** |  | [optional] 
**m_fl_crit_bonus_end** | **float** |  | [optional] 
**m_fl_crit_bonus_end_range** | **float** |  | [optional] 
**m_fl_crit_bonus_start** | **float** |  | [optional] 
**m_fl_crit_bonus_start_range** | **float** |  | [optional] 
**m_fl_cycle_time** | **float** |  | [optional] 
**m_fl_intra_burst_cycle_time** | **float** |  | [optional] 
**m_fl_max_spin_cycle_time** | **float** |  | [optional] 
**m_fl_damage_falloff_bias** | **float** |  | [optional] 
**m_fl_damage_falloff_end_range** | **float** |  | [optional] 
**m_fl_damage_falloff_end_scale** | **float** |  | [optional] 
**m_fl_damage_falloff_start_range** | **float** |  | [optional] 
**m_fl_damage_falloff_start_scale** | **float** |  | [optional] 
**m_fl_horizontal_punch** | **float** |  | [optional] 
**m_fl_range** | **float** |  | [optional] 
**m_fl_recoil_recovery_delay_factor** | **float** |  | [optional] 
**m_fl_recoil_recovery_speed** | **float** |  | [optional] 
**m_fl_recoil_shot_index_recovery_time_factor** | **float** |  | [optional] 
**m_fl_recoil_speed** | **float** |  | [optional] 
**m_fl_reload_move_speed** | **float** |  | [optional] 
**m_fl_scatter_yaw_scale** | **float** |  | [optional] 
**m_aiming_shoot_spread_penalty** | [**MAimingshootspreadpenalty**](MAimingshootspreadpenalty.md) |  | [optional] 
**m_standing_shoot_spread_penalty** | [**MStandingshootspreadpenalty**](MStandingshootspreadpenalty.md) |  | [optional] 
**m_fl_shoot_move_speed_percent** | **float** |  | [optional] 
**m_fl_shoot_spread_penalty_decay** | **float** |  | [optional] 
**m_fl_shoot_spread_penalty_decay_delay** | **float** |  | [optional] 
**m_fl_shoot_spread_penalty_per_shot** | **float** |  | [optional] 
**m_fl_shooting_up_spread_penalty** | **float** |  | [optional] 
**m_fl_vertical_punch** | **float** |  | [optional] 
**m_fl_zoom_fov** | **float** |  | [optional] 
**m_fl_zoom_move_speed_percent** | **float** |  | [optional] 
**m_i_bullets** | **int** |  | [optional] 
**m_i_burst_shot_count** | **int** |  | [optional] 
**m_i_clip_size** | **int** |  | [optional] 
**m_fl_spread** | **float** |  | [optional] 
**m_fl_standing_spread** | **float** |  | [optional] 
**m_fl_low_ammo_indicator_threshold** | **float** |  | [optional] 
**m_fl_recoil_seed** | **float** |  | [optional] 
**m_fl_reload_duration** | **float** |  | [optional] 
**m_bullet_speed_curve** | [**RawItemWeaponInfoBulletSpeedCurveV2Input**](RawItemWeaponInfoBulletSpeedCurveV2Input.md) |  | [optional] 
**m_horizontal_recoil** | [**RawWeaponInfoHorizontalRecoilV2Input**](RawWeaponInfoHorizontalRecoilV2Input.md) |  | [optional] 
**m_vertical_recoil** | [**RawWeaponInfoVerticalRecoilV2Input**](RawWeaponInfoVerticalRecoilV2Input.md) |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.raw_weapon_info_v2_input import RawWeaponInfoV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of RawWeaponInfoV2Input from a JSON string
raw_weapon_info_v2_input_instance = RawWeaponInfoV2Input.from_json(json)
# print the JSON string representation of the object
print(RawWeaponInfoV2Input.to_json())

# convert the object into a dict
raw_weapon_info_v2_input_dict = raw_weapon_info_v2_input_instance.to_dict()
# create an instance of RawWeaponInfoV2Input from a dict
raw_weapon_info_v2_input_from_dict = RawWeaponInfoV2Input.from_dict(raw_weapon_info_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


