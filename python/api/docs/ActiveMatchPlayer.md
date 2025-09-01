# ActiveMatchPlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abandoned** | **bool** |  | [optional] 
**account_id** | **int** |  | [optional] 
**hero_id** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 
**team** | **int** |  | [optional] 
**team_parsed** | [**ActiveMatchTeam**](ActiveMatchTeam.md) |  | [optional] 

## Example

```python
from deadlock-api-client.models.active_match_player import ActiveMatchPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveMatchPlayer from a JSON string
active_match_player_instance = ActiveMatchPlayer.from_json(json)
# print the JSON string representation of the object
print(ActiveMatchPlayer.to_json())

# convert the object into a dict
active_match_player_dict = active_match_player_instance.to_dict()
# create an instance of ActiveMatchPlayer from a dict
active_match_player_from_dict = ActiveMatchPlayer.from_dict(active_match_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


