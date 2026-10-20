# ActiveMatchTeamStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brawl_score** | **int** |  | [optional] 
**net_worth** | **int** |  | [optional] 
**objectives_mask** | **int** |  | [optional] 
**team** | **int** |  | [optional] 
**team_parsed** | [**ActiveMatchTeam**](ActiveMatchTeam.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.active_match_team_stats import ActiveMatchTeamStats

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveMatchTeamStats from a JSON string
active_match_team_stats_instance = ActiveMatchTeamStats.from_json(json)
# print the JSON string representation of the object
print(ActiveMatchTeamStats.to_json())

# convert the object into a dict
active_match_team_stats_dict = active_match_team_stats_instance.to_dict()
# create an instance of ActiveMatchTeamStats from a dict
active_match_team_stats_from_dict = ActiveMatchTeamStats.from_dict(active_match_team_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


