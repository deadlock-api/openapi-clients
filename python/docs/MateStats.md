# MateStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | **List[int]** |  | 
**matches_played** | **int** |  | 
**mate_id** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from deadlock_api_client.models.mate_stats import MateStats

# TODO update the JSON string below
json = "{}"
# create an instance of MateStats from a JSON string
mate_stats_instance = MateStats.from_json(json)
# print the JSON string representation of the object
print(MateStats.to_json())

# convert the object into a dict
mate_stats_dict = mate_stats_instance.to_dict()
# create an instance of MateStats from a dict
mate_stats_from_dict = MateStats.from_dict(mate_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


