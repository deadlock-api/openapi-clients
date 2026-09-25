# ListSteamAccountsResponse

Response for listing Steam accounts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[SteamAccountListItem]**](SteamAccountListItem.md) |  | 
**summary** | [**SlotsSummary**](SlotsSummary.md) |  | 

## Example

```python
from deadlock_api_client.models.list_steam_accounts_response import ListSteamAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSteamAccountsResponse from a JSON string
list_steam_accounts_response_instance = ListSteamAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(ListSteamAccountsResponse.to_json())

# convert the object into a dict
list_steam_accounts_response_dict = list_steam_accounts_response_instance.to_dict()
# create an instance of ListSteamAccountsResponse from a dict
list_steam_accounts_response_from_dict = ListSteamAccountsResponse.from_dict(list_steam_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


