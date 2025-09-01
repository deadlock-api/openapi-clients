# ActiveMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compat_version** | **int** |  | [optional] 
**duration_s** | **int** |  | [optional] 
**game_mode** | **int** |  | [optional] 
**game_mode_parsed** | [**ActiveMatchGameMode**](ActiveMatchGameMode.md) |  | [optional] 
**game_mode_version** | **int** |  | [optional] 
**lobby_id** | **int** |  | [optional] 
**match_id** | **int** |  | [optional] 
**match_mode** | **int** |  | [optional] 
**match_mode_parsed** | [**ActiveMatchMode**](ActiveMatchMode.md) |  | [optional] 
**match_score** | **int** |  | [optional] 
**net_worth_team_0** | **int** |  | [optional] 
**net_worth_team_1** | **int** |  | [optional] 
**objectives_mask_team0** | **int** |  | [optional] 
**objectives_mask_team1** | **int** |  | [optional] 
**open_spectator_slots** | **int** |  | [optional] 
**players** | [**List[ActiveMatchPlayer]**](ActiveMatchPlayer.md) |  | 
**region_mode** | **int** |  | [optional] 
**region_mode_parsed** | [**ActiveMatchRegionMode**](ActiveMatchRegionMode.md) |  | [optional] 
**spectators** | **int** |  | [optional] 
**start_time** | **int** |  | [optional] 
**winning_team** | **int** |  | [optional] 
**winning_team_parsed** | [**ActiveMatchTeam**](ActiveMatchTeam.md) |  | [optional] 

## Example

```python
from deadlock-api-client.models.active_match import ActiveMatch

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveMatch from a JSON string
active_match_instance = ActiveMatch.from_json(json)
# print the JSON string representation of the object
print(ActiveMatch.to_json())

# convert the object into a dict
active_match_dict = active_match_instance.to_dict()
# create an instance of ActiveMatch from a dict
active_match_from_dict = ActiveMatch.from_dict(active_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


