# RawHeroStatsDisplayV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_vec_health_header_stats** | **List[str]** |  | 
**m_vec_magic_header_stats** | **List[str]** |  | 
**m_vec_magic_stats** | **List[str]** |  | 
**m_vec_weapon_header_stats** | **List[str]** |  | 
**m_vec_weapon_stats** | **List[str]** |  | 

## Example

```python
from assets-deadlock-api-client.models.raw_hero_stats_display_v2_input import RawHeroStatsDisplayV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of RawHeroStatsDisplayV2Input from a JSON string
raw_hero_stats_display_v2_input_instance = RawHeroStatsDisplayV2Input.from_json(json)
# print the JSON string representation of the object
print(RawHeroStatsDisplayV2Input.to_json())

# convert the object into a dict
raw_hero_stats_display_v2_input_dict = raw_hero_stats_display_v2_input_instance.to_dict()
# create an instance of RawHeroStatsDisplayV2Input from a dict
raw_hero_stats_display_v2_input_from_dict = RawHeroStatsDisplayV2Input.from_dict(raw_hero_stats_display_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


