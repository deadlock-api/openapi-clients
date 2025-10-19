# RawHeroStatsUIV2Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weapon_stat_display** | **str** |  | 
**display_stats** | [**List[RawHeroStatsUIDisplayV2Output]**](RawHeroStatsUIDisplayV2Output.md) |  | 

## Example

```python
from assets-deadlock-api-client.models.raw_hero_stats_uiv2_output import RawHeroStatsUIV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of RawHeroStatsUIV2Output from a JSON string
raw_hero_stats_uiv2_output_instance = RawHeroStatsUIV2Output.from_json(json)
# print the JSON string representation of the object
print(RawHeroStatsUIV2Output.to_json())

# convert the object into a dict
raw_hero_stats_uiv2_output_dict = raw_hero_stats_uiv2_output_instance.to_dict()
# create an instance of RawHeroStatsUIV2Output from a dict
raw_hero_stats_uiv2_output_from_dict = RawHeroStatsUIV2Output.from_dict(raw_hero_stats_uiv2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


