# ServerStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** | The server ID that reported status | 
**ttl_secs** | **int** | TTL in seconds before this registration expires | 

## Example

```python
from deadlock_api_client.models.server_status_response import ServerStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServerStatusResponse from a JSON string
server_status_response_instance = ServerStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ServerStatusResponse.to_json())

# convert the object into a dict
server_status_response_dict = server_status_response_instance.to_dict()
# create an instance of ServerStatusResponse from a dict
server_status_response_from_dict = ServerStatusResponse.from_dict(server_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


