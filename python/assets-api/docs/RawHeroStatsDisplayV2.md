# RawHeroStatsDisplayV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_header_stats** | **List[str]** |  | 
**health_stats** | **List[str]** |  | 
**magic_header_stats** | **List[str]** |  | 
**magic_stats** | **List[str]** |  | 
**weapon_header_stats** | **List[str]** |  | 
**weapon_stats** | **List[str]** |  | 

## Example

```python
from openapi_client.models.raw_hero_stats_display_v2 import RawHeroStatsDisplayV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawHeroStatsDisplayV2 from a JSON string
raw_hero_stats_display_v2_instance = RawHeroStatsDisplayV2.from_json(json)
# print the JSON string representation of the object
print(RawHeroStatsDisplayV2.to_json())

# convert the object into a dict
raw_hero_stats_display_v2_dict = raw_hero_stats_display_v2_instance.to_dict()
# create an instance of RawHeroStatsDisplayV2 from a dict
raw_hero_stats_display_v2_from_dict = RawHeroStatsDisplayV2.from_dict(raw_hero_stats_display_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


