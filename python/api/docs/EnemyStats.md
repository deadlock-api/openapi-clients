# EnemyStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enemy_id** | **int** |  | 
**matches** | **List[int]** |  | 
**matches_played** | **int** |  | 
**wins** | **int** | The amount of matches won against the enemy. | 

## Example

```python
from openapi_client.models.enemy_stats import EnemyStats

# TODO update the JSON string below
json = "{}"
# create an instance of EnemyStats from a JSON string
enemy_stats_instance = EnemyStats.from_json(json)
# print the JSON string representation of the object
print(EnemyStats.to_json())

# convert the object into a dict
enemy_stats_dict = enemy_stats_instance.to_dict()
# create an instance of EnemyStats from a dict
enemy_stats_from_dict = EnemyStats.from_dict(enemy_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


