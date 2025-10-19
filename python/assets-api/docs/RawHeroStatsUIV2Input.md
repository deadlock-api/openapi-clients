# RawHeroStatsUIV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_e_weapon_stat_display** | **str** |  | 
**m_vec_display_stats** | [**List[RawHeroStatsUIDisplayV2Input]**](RawHeroStatsUIDisplayV2Input.md) |  | 

## Example

```python
from assets-deadlock-api-client.models.raw_hero_stats_uiv2_input import RawHeroStatsUIV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of RawHeroStatsUIV2Input from a JSON string
raw_hero_stats_uiv2_input_instance = RawHeroStatsUIV2Input.from_json(json)
# print the JSON string representation of the object
print(RawHeroStatsUIV2Input.to_json())

# convert the object into a dict
raw_hero_stats_uiv2_input_dict = raw_hero_stats_uiv2_input_instance.to_dict()
# create an instance of RawHeroStatsUIV2Input from a dict
raw_hero_stats_uiv2_input_from_dict = RawHeroStatsUIV2Input.from_dict(raw_hero_stats_uiv2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


