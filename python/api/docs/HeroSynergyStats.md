# HeroSynergyStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists1** | **int** | The number of assists by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**assists2** | **int** | The number of assists by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**creeps1** | **int** | The number of creeps killed by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**creeps2** | **int** | The number of creeps killed by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**deaths1** | **int** | The number of deaths by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**deaths2** | **int** | The number of deaths by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**denies1** | **int** | The number of denies by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**denies2** | **int** | The number of denies by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**hero_id1** | **int** | The ID of the first hero in the pair. | 
**hero_id2** | **int** | The ID of the second hero in the pair. | 
**kills1** | **int** | The number of kills by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**kills2** | **int** | The number of kills by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**last_hits1** | **int** | The number of last hits by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**last_hits2** | **int** | The number of last hits by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**matches_played** | **int** | The total number of matches played where &#x60;hero_id1&#x60; and &#x60;hero_id2&#x60; were on the same team, meeting the filter criteria. | 
**networth1** | **int** | The net worth of &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**networth2** | **int** | The net worth of &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**obj_damage1** | **int** | The amount of objective damage dealt by &#x60;hero_id1&#x60; when playing with &#x60;hero_id2&#x60;. | 
**obj_damage2** | **int** | The amount of objective damage dealt by &#x60;hero_id2&#x60; when playing with &#x60;hero_id1&#x60;. | 
**wins** | **int** | The number of times the team won when both &#x60;hero_id1&#x60; and &#x60;hero_id2&#x60; were on the same team. | 

## Example

```python
from openapi_client.models.hero_synergy_stats import HeroSynergyStats

# TODO update the JSON string below
json = "{}"
# create an instance of HeroSynergyStats from a JSON string
hero_synergy_stats_instance = HeroSynergyStats.from_json(json)
# print the JSON string representation of the object
print(HeroSynergyStats.to_json())

# convert the object into a dict
hero_synergy_stats_dict = hero_synergy_stats_instance.to_dict()
# create an instance of HeroSynergyStats from a dict
hero_synergy_stats_from_dict = HeroSynergyStats.from_dict(hero_synergy_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


