# GameServerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_player_count** | **int** |  | 
**game_mode** | **str** |  | 
**ip** | **str** |  | 
**last_updated** | **str** |  | 
**port** | **int** |  | 
**region** | **str** |  | 
**server_id** | **str** |  | 

## Example

```python
from deadlock_api_client.models.game_server_info import GameServerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GameServerInfo from a JSON string
game_server_info_instance = GameServerInfo.from_json(json)
# print the JSON string representation of the object
print(GameServerInfo.to_json())

# convert the object into a dict
game_server_info_dict = game_server_info_instance.to_dict()
# create an instance of GameServerInfo from a dict
game_server_info_from_dict = GameServerInfo.from_dict(game_server_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


