# ServerStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_player_count** | **int** | Current number of players on this server | 
**game_mode** | **str** | Game mode this server is running (e.g. \&quot;ranked\&quot;, \&quot;unranked\&quot;) | 
**hostname** | **str** | Hostname of the game server | [optional] 
**ip** | **str** | IP address of the game server | 
**port** | **int** | Port the game server is listening on | 
**region** | **str** | Region the server is located in (e.g. \&quot;eu\&quot;, \&quot;na\&quot;, \&quot;sa\&quot;, \&quot;asia\&quot;, \&quot;oceania\&quot;) | 
**server_id** | **str** | Unique identifier for the game server | 

## Example

```python
from deadlock_api_client.models.server_status_request import ServerStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServerStatusRequest from a JSON string
server_status_request_instance = ServerStatusRequest.from_json(json)
# print the JSON string representation of the object
print(ServerStatusRequest.to_json())

# convert the object into a dict
server_status_request_dict = server_status_request_instance.to_dict()
# create an instance of ServerStatusRequest from a dict
server_status_request_from_dict = ServerStatusRequest.from_dict(server_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


