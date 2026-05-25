# PlayerAccountStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**stats** | [**List[PlayerAccountHeroStats]**](PlayerAccountHeroStats.md) |  | 

## Example

```python
from deadlock_api_client.models.player_account_stats import PlayerAccountStats

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerAccountStats from a JSON string
player_account_stats_instance = PlayerAccountStats.from_json(json)
# print the JSON string representation of the object
print(PlayerAccountStats.to_json())

# convert the object into a dict
player_account_stats_dict = player_account_stats_instance.to_dict()
# create an instance of PlayerAccountStats from a dict
player_account_stats_from_dict = PlayerAccountStats.from_dict(player_account_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


