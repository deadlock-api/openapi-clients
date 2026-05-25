# PlayerAccountHeroStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hero_id** | **int** |  | [optional] 
**medals_bronze** | **List[int]** |  | 
**medals_gold** | **List[int]** |  | 
**medals_silver** | **List[int]** |  | 
**stat_id** | **List[int]** |  | 
**total_value** | **List[int]** |  | 

## Example

```python
from deadlock_api_client.models.player_account_hero_stats import PlayerAccountHeroStats

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerAccountHeroStats from a JSON string
player_account_hero_stats_instance = PlayerAccountHeroStats.from_json(json)
# print the JSON string representation of the object
print(PlayerAccountHeroStats.to_json())

# convert the object into a dict
player_account_hero_stats_dict = player_account_hero_stats_instance.to_dict()
# create an instance of PlayerAccountHeroStats from a dict
player_account_hero_stats_from_dict = PlayerAccountHeroStats.from_dict(player_account_hero_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


