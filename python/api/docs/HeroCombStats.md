# HeroCombStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hero_ids** | **List[int]** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**losses** | **int** |  | 
**matches** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from deadlock_api_client.models.hero_comb_stats import HeroCombStats

# TODO update the JSON string below
json = "{}"
# create an instance of HeroCombStats from a JSON string
hero_comb_stats_instance = HeroCombStats.from_json(json)
# print the JSON string representation of the object
print(HeroCombStats.to_json())

# convert the object into a dict
hero_comb_stats_dict = hero_comb_stats_instance.to_dict()
# create an instance of HeroCombStats from a dict
hero_comb_stats_from_dict = HeroCombStats.from_dict(hero_comb_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


