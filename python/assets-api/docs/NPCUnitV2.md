# NPCUnitV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | 
**weapon_info** | [**RawWeaponInfoV2**](RawWeaponInfoV2.md) |  | [optional] 
**max_health** | **int** |  | [optional] 
**sight_range_players** | **float** |  | [optional] 
**sight_range_npcs** | **float** |  | [optional] 
**gold_reward** | **float** |  | [optional] 
**gold_reward_bonus_percent_per_minute** | **float** |  | [optional] 
**m_fl_player_damage_resist_pct** | **float** |  | [optional] 
**trooper_damage_resist_pct** | **float** |  | [optional] 
**t1_boss_damage_resist_pct** | **float** |  | [optional] 
**t2_boss_damage_resist_pct** | **float** |  | [optional] 
**t3_boss_damage_resist_pct** | **float** |  | [optional] 
**barrack_guardian_damage_resist_pct** | **float** |  | [optional] 
**near_death_duration** | **float** |  | [optional] 
**walk_speed** | **float** |  | [optional] 
**run_speed** | **float** |  | [optional] 
**acceleration** | **float** |  | [optional] 
**melee_damage** | **float** |  | [optional] 
**melee_attempt_range** | **float** |  | [optional] 
**melee_hit_range** | **float** |  | [optional] 
**melee_duration** | **float** |  | [optional] 
**attack_t1_boss_max_range** | **float** |  | [optional] 
**attack_t3_boss_max_range** | **float** |  | [optional] 
**attack_t3_boss_phase2_max_range** | **float** |  | [optional] 
**attack_trooper_max_range** | **float** |  | [optional] 
**t1_boss_dps** | **float** |  | [optional] 
**t1_boss_dpsbase_resist** | **float** |  | [optional] 
**t1_boss_dpsmax_resist** | **float** |  | [optional] 
**t1_boss_dpsmax_resist_time_in_seconds** | **float** |  | [optional] 
**t2_boss_dps** | **float** |  | [optional] 
**t2_boss_dpsbase_resist** | **float** |  | [optional] 
**t2_boss_dpsmax_resist** | **float** |  | [optional] 
**t2_boss_dpsmax_resist_time_in_seconds** | **float** |  | [optional] 
**t3_boss_dps** | **float** |  | [optional] 
**generator_boss_dps** | **float** |  | [optional] 
**barrack_boss_dps** | **float** |  | [optional] 
**player_dps** | **float** |  | [optional] 
**trooper_dps** | **float** |  | [optional] 
**health_bar_color_friend** | [**ColorV1**](ColorV1.md) |  | [optional] 
**health_bar_color_enemy** | [**ColorV1**](ColorV1.md) |  | [optional] 
**health_bar_color_team1** | [**ColorV1**](ColorV1.md) |  | [optional] 
**health_bar_color_team2** | [**ColorV1**](ColorV1.md) |  | [optional] 
**health_bar_color_team_neutral** | [**ColorV1**](ColorV1.md) |  | [optional] 
**glow_color_friend** | [**ColorV1**](ColorV1.md) |  | [optional] 
**glow_color_enemy** | [**ColorV1**](ColorV1.md) |  | [optional] 
**glow_color_team1** | [**ColorV1**](ColorV1.md) |  | [optional] 
**glow_color_team2** | [**ColorV1**](ColorV1.md) |  | [optional] 
**glow_color_team_neutral** | [**ColorV1**](ColorV1.md) |  | [optional] 
**id** | **int** |  | [readonly] 

## Example

```python
from assets_deadlock_api_client.models.npc_unit_v2 import NPCUnitV2

# TODO update the JSON string below
json = "{}"
# create an instance of NPCUnitV2 from a JSON string
npc_unit_v2_instance = NPCUnitV2.from_json(json)
# print the JSON string representation of the object
print(NPCUnitV2.to_json())

# convert the object into a dict
npc_unit_v2_dict = npc_unit_v2_instance.to_dict()
# create an instance of NPCUnitV2 from a dict
npc_unit_v2_from_dict = NPCUnitV2.from_dict(npc_unit_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


