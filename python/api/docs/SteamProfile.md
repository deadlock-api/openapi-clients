# SteamProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**avatar** | **str** |  | 
**avatarfull** | **str** |  | 
**avatarmedium** | **str** |  | 
**countrycode** | **str** |  | [optional] 
**last_updated** | **datetime** |  | 
**personaname** | **str** |  | 
**profileurl** | **str** |  | 
**realname** | **str** |  | [optional] 

## Example

```python
from deadlock-api-client.models.steam_profile import SteamProfile

# TODO update the JSON string below
json = "{}"
# create an instance of SteamProfile from a JSON string
steam_profile_instance = SteamProfile.from_json(json)
# print the JSON string representation of the object
print(SteamProfile.to_json())

# convert the object into a dict
steam_profile_dict = steam_profile_instance.to_dict()
# create an instance of SteamProfile from a dict
steam_profile_from_dict = SteamProfile.from_dict(steam_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


