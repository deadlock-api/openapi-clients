# HeroStartingStatsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_move_speed** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**sprint_speed** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**crouch_speed** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**move_acceleration** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**light_melee_damage** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**heavy_melee_damage** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**max_health** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**weapon_power** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**reload_speed** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**weapon_power_scale** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**proc_build_up_rate_scale** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**stamina** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**base_health_regen** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**stamina_regen_per_second** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**ability_resource_max** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**ability_resource_regen_per_second** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**crit_damage_received_scale** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**tech_duration** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**tech_armor_damage_reduction** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | [optional] 
**tech_range** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | 
**bullet_armor_damage_reduction** | [**HeroStartingStatV2**](HeroStartingStatV2.md) |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.hero_starting_stats_v2 import HeroStartingStatsV2

# TODO update the JSON string below
json = "{}"
# create an instance of HeroStartingStatsV2 from a JSON string
hero_starting_stats_v2_instance = HeroStartingStatsV2.from_json(json)
# print the JSON string representation of the object
print(HeroStartingStatsV2.to_json())

# convert the object into a dict
hero_starting_stats_v2_dict = hero_starting_stats_v2_instance.to_dict()
# create an instance of HeroStartingStatsV2 from a dict
hero_starting_stats_v2_from_dict = HeroStartingStatsV2.from_dict(hero_starting_stats_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


