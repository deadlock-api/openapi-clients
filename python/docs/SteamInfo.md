# SteamInfo

Per-patch Steam manifest as served by the public assets API.  Field order is load-bearing — it sets the JSON key order, which matches the legacy Python endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** |  | 
**client_version** | **int** |  | 
**product_name** | **str** |  | 
**server_app_id** | **int** |  | 
**server_version** | **int** |  | 
**source_revision** | **int** |  | 
**tools_app_id** | **int** |  | 
**version_date** | **str** |  | 
**version_datetime** | **str** | &#x60;version_date&#x60; + &#x60;version_time&#x60; combined into a naive ISO-8601 string (&#x60;YYYY-MM-DDTHH:MM:SS&#x60;, no timezone) — matches the Python output. | 
**version_time** | **str** |  | 

## Example

```python
from deadlock_api_client.models.steam_info import SteamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SteamInfo from a JSON string
steam_info_instance = SteamInfo.from_json(json)
# print the JSON string representation of the object
print(SteamInfo.to_json())

# convert the object into a dict
steam_info_dict = steam_info_instance.to_dict()
# create an instance of SteamInfo from a dict
steam_info_from_dict = SteamInfo.from_dict(steam_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


