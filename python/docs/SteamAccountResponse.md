# SteamAccountResponse

Response for a Steam account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**deleted_at** | **datetime** |  | [optional] 
**id** | **UUID** |  | 
**steam_id3** | **int** |  | 

## Example

```python
from deadlock_api_client.models.steam_account_response import SteamAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SteamAccountResponse from a JSON string
steam_account_response_instance = SteamAccountResponse.from_json(json)
# print the JSON string representation of the object
print(SteamAccountResponse.to_json())

# convert the object into a dict
steam_account_response_dict = steam_account_response_instance.to_dict()
# create an instance of SteamAccountResponse from a dict
steam_account_response_from_dict = SteamAccountResponse.from_dict(steam_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


