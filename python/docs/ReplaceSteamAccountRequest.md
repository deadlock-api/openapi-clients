# ReplaceSteamAccountRequest

Request body for replacing a Steam account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**steam_id3** | **int** | New Steam ID3 (32-bit unsigned integer format) | 

## Example

```python
from deadlock_api_client.models.replace_steam_account_request import ReplaceSteamAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceSteamAccountRequest from a JSON string
replace_steam_account_request_instance = ReplaceSteamAccountRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceSteamAccountRequest.to_json())

# convert the object into a dict
replace_steam_account_request_dict = replace_steam_account_request_instance.to_dict()
# create an instance of ReplaceSteamAccountRequest from a dict
replace_steam_account_request_from_dict = ReplaceSteamAccountRequest.from_dict(replace_steam_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


