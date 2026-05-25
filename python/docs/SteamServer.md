# SteamServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addr** | **str** | Full address of the server including port (e.g. &#x60;1.2.3.4:27015&#x60;) | 
**appid** | **int** | Steam appid of the game running on this server | 
**bots** | **int** | Number of bots on the server | 
**dedicated** | **bool** | Whether this is a dedicated server | 
**gamedir** | **str** | Internal game directory name | 
**gameport** | **int** | Game port the server is listening on | 
**gametype** | **str** | Steam gametype tags | 
**map** | **str** | Current map | 
**max_players** | **int** | Maximum player count | 
**name** | **str** | Server name as advertised to Steam | 
**os** | **str** | Operating system the server is running on (e.g. &#x60;l&#x60; for Linux, &#x60;w&#x60; for Windows) | 
**players** | **int** | Current player count | 
**product** | **str** | Product identifier reported by the server | 
**region** | **int** | Steam region code reported by the server | 
**secure** | **bool** | Whether the server is VAC-secured | 
**steamid** | **str** | &#x60;SteamID&#x60; of the server | 
**version** | **str** | Server build version | 

## Example

```python
from deadlock_api_client.models.steam_server import SteamServer

# TODO update the JSON string below
json = "{}"
# create an instance of SteamServer from a JSON string
steam_server_instance = SteamServer.from_json(json)
# print the JSON string representation of the object
print(SteamServer.to_json())

# convert the object into a dict
steam_server_dict = steam_server_instance.to_dict()
# create an instance of SteamServer from a dict
steam_server_from_dict = SteamServer.from_dict(steam_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


