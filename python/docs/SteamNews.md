# SteamNews


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**guid** | [**PatchGuid**](PatchGuid.md) |  | 
**link** | **str** |  | 
**pub_date** | **datetime** |  | 
**title** | **str** |  | 

## Example

```python
from deadlock_api_client.models.steam_news import SteamNews

# TODO update the JSON string below
json = "{}"
# create an instance of SteamNews from a JSON string
steam_news_instance = SteamNews.from_json(json)
# print the JSON string representation of the object
print(SteamNews.to_json())

# convert the object into a dict
steam_news_dict = steam_news_instance.to_dict()
# create an instance of SteamNews from a dict
steam_news_from_dict = SteamNews.from_dict(steam_news_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


