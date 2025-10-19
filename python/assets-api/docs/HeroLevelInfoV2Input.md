# HeroLevelInfoV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_b_use_standard_upgrade** | **bool** |  | [optional] 
**bonus_currencies** | **List[str]** |  | [optional] 
**m_un_required_gold** | **int** |  | 

## Example

```python
from assets-deadlock-api-client.models.hero_level_info_v2_input import HeroLevelInfoV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of HeroLevelInfoV2Input from a JSON string
hero_level_info_v2_input_instance = HeroLevelInfoV2Input.from_json(json)
# print the JSON string representation of the object
print(HeroLevelInfoV2Input.to_json())

# convert the object into a dict
hero_level_info_v2_input_dict = hero_level_info_v2_input_instance.to_dict()
# create an instance of HeroLevelInfoV2Input from a dict
hero_level_info_v2_input_from_dict = HeroLevelInfoV2Input.from_dict(hero_level_info_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


