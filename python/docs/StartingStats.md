# StartingStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ability_resource_max** | [**StartingStat**](StartingStat.md) |  | 
**ability_resource_regen_per_second** | [**StartingStat**](StartingStat.md) |  | 
**base_health_regen** | [**StartingStat**](StartingStat.md) |  | 
**bullet_armor_damage_reduction** | [**StartingStat**](StartingStat.md) |  | [optional] 
**crit_damage_received_scale** | [**StartingStat**](StartingStat.md) |  | 
**crouch_speed** | [**StartingStat**](StartingStat.md) |  | 
**heavy_melee_damage** | [**StartingStat**](StartingStat.md) |  | 
**light_melee_damage** | [**StartingStat**](StartingStat.md) |  | 
**max_health** | [**StartingStat**](StartingStat.md) |  | 
**max_move_speed** | [**StartingStat**](StartingStat.md) |  | 
**move_acceleration** | [**StartingStat**](StartingStat.md) |  | 
**proc_build_up_rate_scale** | [**StartingStat**](StartingStat.md) |  | 
**reload_speed** | [**StartingStat**](StartingStat.md) |  | 
**sprint_speed** | [**StartingStat**](StartingStat.md) |  | 
**stamina** | [**StartingStat**](StartingStat.md) |  | 
**stamina_regen_per_second** | [**StartingStat**](StartingStat.md) |  | 
**tech_armor_damage_reduction** | [**StartingStat**](StartingStat.md) |  | [optional] 
**tech_duration** | [**StartingStat**](StartingStat.md) |  | 
**tech_range** | [**StartingStat**](StartingStat.md) |  | 
**weapon_power** | [**StartingStat**](StartingStat.md) |  | 
**weapon_power_scale** | [**StartingStat**](StartingStat.md) |  | 

## Example

```python
from deadlock_api_client.models.starting_stats import StartingStats

# TODO update the JSON string below
json = "{}"
# create an instance of StartingStats from a JSON string
starting_stats_instance = StartingStats.from_json(json)
# print the JSON string representation of the object
print(StartingStats.to_json())

# convert the object into a dict
starting_stats_dict = starting_stats_instance.to_dict()
# create an instance of StartingStats from a dict
starting_stats_from_dict = StartingStats.from_dict(starting_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


