# RawHeroStatsDisplayV2Output


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
from assets-deadlock-api-client.models.raw_hero_stats_display_v2_output import RawHeroStatsDisplayV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of RawHeroStatsDisplayV2Output from a JSON string
raw_hero_stats_display_v2_output_instance = RawHeroStatsDisplayV2Output.from_json(json)
# print the JSON string representation of the object
print(RawHeroStatsDisplayV2Output.to_json())

# convert the object into a dict
raw_hero_stats_display_v2_output_dict = raw_hero_stats_display_v2_output_instance.to_dict()
# create an instance of RawHeroStatsDisplayV2Output from a dict
raw_hero_stats_display_v2_output_from_dict = RawHeroStatsDisplayV2Output.from_dict(raw_hero_stats_display_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


