# PlayerMatchHistoryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abandoned_time_s** | **int** |  | [optional] 
**account_id** | **int** |  | 
**brawl_avg_round_time_s** | **int** |  | [optional] 
**brawl_score_team0** | **int** |  | [optional] 
**brawl_score_team1** | **int** |  | [optional] 
**denies** | **int** |  | 
**game_mode** | **int** |  | 
**hero_id** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**hero_level** | **int** |  | 
**last_hits** | **int** |  | 
**match_duration_s** | **int** |  | 
**match_id** | **int** |  | 
**match_mode** | **int** |  | 
**match_result** | **int** |  | 
**net_worth** | **int** |  | 
**objectives_mask_team0** | **int** |  | 
**objectives_mask_team1** | **int** |  | 
**player_assists** | **int** |  | 
**player_deaths** | **int** |  | 
**player_kills** | **int** |  | 
**player_team** | **int** |  | 
**start_time** | **int** |  | 
**team_abandoned** | **bool** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from deadlock_api_client.models.player_match_history_entry import PlayerMatchHistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerMatchHistoryEntry from a JSON string
player_match_history_entry_instance = PlayerMatchHistoryEntry.from_json(json)
# print the JSON string representation of the object
print(PlayerMatchHistoryEntry.to_json())

# convert the object into a dict
player_match_history_entry_dict = player_match_history_entry_instance.to_dict()
# create an instance of PlayerMatchHistoryEntry from a dict
player_match_history_entry_from_dict = PlayerMatchHistoryEntry.from_dict(player_match_history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


