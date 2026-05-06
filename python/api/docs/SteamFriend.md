# SteamFriend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**friend_since** | **datetime** |  | 

## Example

```python
from deadlock_api_client.models.steam_friend import SteamFriend

# TODO update the JSON string below
json = "{}"
# create an instance of SteamFriend from a JSON string
steam_friend_instance = SteamFriend.from_json(json)
# print the JSON string representation of the object
print(SteamFriend.to_json())

# convert the object into a dict
steam_friend_dict = steam_friend_instance.to_dict()
# create an instance of SteamFriend from a dict
steam_friend_from_dict = SteamFriend.from_dict(steam_friend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


