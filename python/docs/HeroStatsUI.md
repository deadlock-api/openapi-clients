# HeroStatsUI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_stats** | [**List[HeroStatsUIDisplay]**](HeroStatsUIDisplay.md) |  | 
**weapon_stat_display** | **str** |  | 

## Example

```python
from deadlock_api_client.models.hero_stats_ui import HeroStatsUI

# TODO update the JSON string below
json = "{}"
# create an instance of HeroStatsUI from a JSON string
hero_stats_ui_instance = HeroStatsUI.from_json(json)
# print the JSON string representation of the object
print(HeroStatsUI.to_json())

# convert the object into a dict
hero_stats_ui_dict = hero_stats_ui_instance.to_dict()
# create an instance of HeroStatsUI from a dict
hero_stats_ui_from_dict = HeroStatsUI.from_dict(hero_stats_ui_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


