# RawHeroStatsUIV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weapon_stat_display** | **str** |  | 
**display_stats** | [**List[RawHeroStatsUIDisplayV2]**](RawHeroStatsUIDisplayV2.md) |  | 

## Example

```python
from assets-deadlock-api-client.models.raw_hero_stats_uiv2 import RawHeroStatsUIV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawHeroStatsUIV2 from a JSON string
raw_hero_stats_uiv2_instance = RawHeroStatsUIV2.from_json(json)
# print the JSON string representation of the object
print(RawHeroStatsUIV2.to_json())

# convert the object into a dict
raw_hero_stats_uiv2_dict = raw_hero_stats_uiv2_instance.to_dict()
# create an instance of RawHeroStatsUIV2 from a dict
raw_hero_stats_uiv2_from_dict = RawHeroStatsUIV2.from_dict(raw_hero_stats_uiv2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


