# HeroStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**accuracy** | **float** |  | 
**assists** | **int** |  | 
**assists_per_min** | **float** |  | 
**creeps_per_min** | **float** |  | 
**crit_shot_rate** | **float** |  | 
**damage_mitigated_per_min** | **float** |  | 
**damage_per_min** | **float** |  | 
**damage_per_soul** | **float** |  | 
**damage_taken_per_min** | **float** |  | 
**damage_taken_per_soul** | **float** |  | 
**deaths** | **int** |  | 
**deaths_per_min** | **float** |  | 
**denies_per_match** | **float** |  | 
**denies_per_min** | **float** |  | 
**ending_level** | **float** |  | 
**hero_id** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**kills** | **int** |  | 
**kills_per_min** | **float** |  | 
**last_hits_per_min** | **float** |  | 
**last_played** | **int** |  | 
**matches** | **List[int]** |  | 
**matches_played** | **int** |  | 
**networth_per_min** | **float** |  | 
**obj_damage_per_min** | **float** |  | 
**obj_damage_per_soul** | **float** |  | 
**time_played** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from deadlock-api-client.models.hero_stats import HeroStats

# TODO update the JSON string below
json = "{}"
# create an instance of HeroStats from a JSON string
hero_stats_instance = HeroStats.from_json(json)
# print the JSON string representation of the object
print(HeroStats.to_json())

# convert the object into a dict
hero_stats_dict = hero_stats_instance.to_dict()
# create an instance of HeroStats from a dict
hero_stats_from_dict = HeroStats.from_dict(hero_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


