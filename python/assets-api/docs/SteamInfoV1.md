# SteamInfoV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_version** | **int** |  | 
**server_version** | **int** |  | 
**product_name** | **str** |  | 
**app_id** | **int** |  | 
**server_app_id** | **int** |  | 
**tools_app_id** | **int** |  | 
**source_revision** | **int** |  | 
**version_date** | **str** |  | 
**version_time** | **str** |  | 
**version_datetime** | **datetime** |  | [readonly] 

## Example

```python
from assets_deadlock_api_client.models.steam_info_v1 import SteamInfoV1

# TODO update the JSON string below
json = "{}"
# create an instance of SteamInfoV1 from a JSON string
steam_info_v1_instance = SteamInfoV1.from_json(json)
# print the JSON string representation of the object
print(SteamInfoV1.to_json())

# convert the object into a dict
steam_info_v1_dict = steam_info_v1_instance.to_dict()
# create an instance of SteamInfoV1 from a dict
steam_info_v1_from_dict = SteamInfoV1.from_dict(steam_info_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


