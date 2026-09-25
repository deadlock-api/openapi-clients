# SteamAccountListItem

Response for a Steam account in the list endpoint (includes `is_in_cooldown`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**deleted_at** | **datetime** |  | [optional] 
**id** | **UUID** |  | 
**is_in_cooldown** | **bool** |  | 
**steam_id3** | **int** |  | 

## Example

```python
from deadlock_api_client.models.steam_account_list_item import SteamAccountListItem

# TODO update the JSON string below
json = "{}"
# create an instance of SteamAccountListItem from a JSON string
steam_account_list_item_instance = SteamAccountListItem.from_json(json)
# print the JSON string representation of the object
print(SteamAccountListItem.to_json())

# convert the object into a dict
steam_account_list_item_dict = steam_account_list_item_instance.to_dict()
# create an instance of SteamAccountListItem from a dict
steam_account_list_item_from_dict = SteamAccountListItem.from_dict(steam_account_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


