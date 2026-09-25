# DeleteSteamAccountResponse

Response for deleting a Steam account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from deadlock_api_client.models.delete_steam_account_response import DeleteSteamAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSteamAccountResponse from a JSON string
delete_steam_account_response_instance = DeleteSteamAccountResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteSteamAccountResponse.to_json())

# convert the object into a dict
delete_steam_account_response_dict = delete_steam_account_response_instance.to_dict()
# create an instance of DeleteSteamAccountResponse from a dict
delete_steam_account_response_from_dict = DeleteSteamAccountResponse.from_dict(delete_steam_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


