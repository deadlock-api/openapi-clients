# KillDeathStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deaths** | **int** |  | 
**kills** | **int** |  | 
**position_x** | **int** |  | 
**position_y** | **int** |  | 

## Example

```python
from deadlock-api-client.models.kill_death_stats import KillDeathStats

# TODO update the JSON string below
json = "{}"
# create an instance of KillDeathStats from a JSON string
kill_death_stats_instance = KillDeathStats.from_json(json)
# print the JSON string representation of the object
print(KillDeathStats.to_json())

# convert the object into a dict
kill_death_stats_dict = kill_death_stats_instance.to_dict()
# create an instance of KillDeathStats from a dict
kill_death_stats_from_dict = KillDeathStats.from_dict(kill_death_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


