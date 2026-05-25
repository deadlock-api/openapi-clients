# ListServersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | [**List[GameServerInfo]**](GameServerInfo.md) |  | 

## Example

```python
from deadlock_api_client.models.list_servers_response import ListServersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListServersResponse from a JSON string
list_servers_response_instance = ListServersResponse.from_json(json)
# print the JSON string representation of the object
print(ListServersResponse.to_json())

# convert the object into a dict
list_servers_response_dict = list_servers_response_instance.to_dict()
# create an instance of ListServersResponse from a dict
list_servers_response_from_dict = ListServersResponse.from_dict(list_servers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


