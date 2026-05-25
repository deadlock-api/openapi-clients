# HeroBuildStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hero_build_id** | **int** | The ID of the hero build. The &#x60;hero_build_id&#x60; is the first build the player had selected when the game started. | 
**hero_id** | **int** | The ID of the hero. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**losses** | **int** | The number of losses with this build. | 
**matches** | **int** | The total number of matches played with this build (&#x60;wins + losses&#x60;). | 
**players** | **int** | The number of unique players who used this build. | 
**wins** | **int** | The number of wins with this build. | 

## Example

```python
from deadlock_api_client.models.hero_build_stats import HeroBuildStats

# TODO update the JSON string below
json = "{}"
# create an instance of HeroBuildStats from a JSON string
hero_build_stats_instance = HeroBuildStats.from_json(json)
# print the JSON string representation of the object
print(HeroBuildStats.to_json())

# convert the object into a dict
hero_build_stats_dict = hero_build_stats_instance.to_dict()
# create an instance of HeroBuildStats from a dict
hero_build_stats_from_dict = HeroBuildStats.from_dict(hero_build_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


