# RawHeroLevelInfoV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_standard_upgrade** | **bool** |  | [optional] 
**bonus_currencies** | **Dict[str, int]** |  | [optional] 
**required_gold** | **int** |  | 

## Example

```python
from assets_deadlock_api_client.models.raw_hero_level_info_v2 import RawHeroLevelInfoV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawHeroLevelInfoV2 from a JSON string
raw_hero_level_info_v2_instance = RawHeroLevelInfoV2.from_json(json)
# print the JSON string representation of the object
print(RawHeroLevelInfoV2.to_json())

# convert the object into a dict
raw_hero_level_info_v2_dict = raw_hero_level_info_v2_instance.to_dict()
# create an instance of RawHeroLevelInfoV2 from a dict
raw_hero_level_info_v2_from_dict = RawHeroLevelInfoV2.from_dict(raw_hero_level_info_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


