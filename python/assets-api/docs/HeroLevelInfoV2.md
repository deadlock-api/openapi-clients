# HeroLevelInfoV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_standard_upgrade** | **bool** |  | [optional] 
**bonus_currencies** | **List[str]** |  | [optional] 
**required_gold** | **int** |  | 

## Example

```python
from assets_deadlock_api_client.models.hero_level_info_v2 import HeroLevelInfoV2

# TODO update the JSON string below
json = "{}"
# create an instance of HeroLevelInfoV2 from a JSON string
hero_level_info_v2_instance = HeroLevelInfoV2.from_json(json)
# print the JSON string representation of the object
print(HeroLevelInfoV2.to_json())

# convert the object into a dict
hero_level_info_v2_dict = hero_level_info_v2_instance.to_dict()
# create an instance of HeroLevelInfoV2 from a dict
hero_level_info_v2_from_dict = HeroLevelInfoV2.from_dict(hero_level_info_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


