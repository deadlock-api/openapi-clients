# HeroStatsUIDisplay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | 
**stat_type** | **str** |  | 

## Example

```python
from deadlock_api_client.models.hero_stats_ui_display import HeroStatsUIDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of HeroStatsUIDisplay from a JSON string
hero_stats_ui_display_instance = HeroStatsUIDisplay.from_json(json)
# print the JSON string representation of the object
print(HeroStatsUIDisplay.to_json())

# convert the object into a dict
hero_stats_ui_display_dict = hero_stats_ui_display_instance.to_dict()
# create an instance of HeroStatsUIDisplay from a dict
hero_stats_ui_display_from_dict = HeroStatsUIDisplay.from_dict(hero_stats_ui_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


