# RawHeroStartingStatsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_move_speed** | **float** |  | 
**sprint_speed** | **float** |  | 
**crouch_speed** | **float** |  | 
**move_acceleration** | **float** |  | 
**light_melee_damage** | **float** |  | 
**heavy_melee_damage** | **int** |  | 
**max_health** | **int** |  | 
**weapon_power** | **int** |  | 
**reload_speed** | **int** |  | 
**weapon_power_scale** | **int** |  | 
**proc_build_up_rate_scale** | **int** |  | 
**stamina** | **int** |  | 
**base_health_regen** | **float** |  | 
**stamina_regen_per_second** | **float** |  | 
**ability_resource_max** | **int** |  | 
**ability_resource_regen_per_second** | **int** |  | 
**crit_damage_received_scale** | **float** |  | 
**tech_duration** | **int** |  | 
**tech_armor_damage_reduction** | **float** |  | [optional] 
**tech_range** | **int** |  | 
**bullet_armor_damage_reduction** | **float** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.raw_hero_starting_stats_v2 import RawHeroStartingStatsV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawHeroStartingStatsV2 from a JSON string
raw_hero_starting_stats_v2_instance = RawHeroStartingStatsV2.from_json(json)
# print the JSON string representation of the object
print(RawHeroStartingStatsV2.to_json())

# convert the object into a dict
raw_hero_starting_stats_v2_dict = raw_hero_starting_stats_v2_instance.to_dict()
# create an instance of RawHeroStartingStatsV2 from a dict
raw_hero_starting_stats_v2_from_dict = RawHeroStartingStatsV2.from_dict(raw_hero_starting_stats_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


