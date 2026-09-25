# AddSteamAccountRequest

Request body for adding a Steam account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**steam_id3** | **int** | Steam ID3 (32-bit unsigned integer format) | 

## Example

```python
from deadlock_api_client.models.add_steam_account_request import AddSteamAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddSteamAccountRequest from a JSON string
add_steam_account_request_instance = AddSteamAccountRequest.from_json(json)
# print the JSON string representation of the object
print(AddSteamAccountRequest.to_json())

# convert the object into a dict
add_steam_account_request_dict = add_steam_account_request_instance.to_dict()
# create an instance of AddSteamAccountRequest from a dict
add_steam_account_request_from_dict = AddSteamAccountRequest.from_dict(add_steam_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


