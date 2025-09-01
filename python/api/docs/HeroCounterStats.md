# HeroCounterStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists** | **int** | The number of assists by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**creeps** | **int** | The number of creeps killed by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**deaths** | **int** | The number of deaths by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**denies** | **int** | The number of denies by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**enemy_assists** | **int** | The number of assists by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**enemy_creeps** | **int** | The number of creeps killed by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**enemy_deaths** | **int** | The number of deaths by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**enemy_denies** | **int** | The number of denies by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**enemy_hero_id** | **int** | The ID of the opposing hero. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**enemy_kills** | **int** | The number of kills by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**enemy_last_hits** | **int** | The number of last hits by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**enemy_networth** | **int** | The net worth of &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**enemy_obj_damage** | **int** | The amount of objective damage dealt by &#x60;enemy_hero_id&#x60; when facing &#x60;hero_id&#x60;. | 
**hero_id** | **int** | The ID of the hero. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**kills** | **int** | The number of kills by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**last_hits** | **int** | The number of last hits by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**matches_played** | **int** | The total number of matches played between &#x60;hero_id&#x60; and &#x60;enemy_hero_id&#x60; that meet the filter criteria. | 
**networth** | **int** | The net worth of &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**obj_damage** | **int** | The amount of objective damage dealt by &#x60;hero_id&#x60; when facing &#x60;enemy_hero_id&#x60;. | 
**wins** | **int** | The number of times &#x60;hero_id&#x60; won the match when facing &#x60;enemy_hero_id&#x60;. | 

## Example

```python
from deadlock-api-client.models.hero_counter_stats import HeroCounterStats

# TODO update the JSON string below
json = "{}"
# create an instance of HeroCounterStats from a JSON string
hero_counter_stats_instance = HeroCounterStats.from_json(json)
# print the JSON string representation of the object
print(HeroCounterStats.to_json())

# convert the object into a dict
hero_counter_stats_dict = hero_counter_stats_instance.to_dict()
# create an instance of HeroCounterStats from a dict
hero_counter_stats_from_dict = HeroCounterStats.from_dict(hero_counter_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


