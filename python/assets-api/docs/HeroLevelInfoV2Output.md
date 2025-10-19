# HeroLevelInfoV2Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_standard_upgrade** | **bool** |  | [optional] 
**bonus_currencies** | **List[str]** |  | [optional] 
**required_gold** | **int** |  | 

## Example

```python
from assets-deadlock-api-client.models.hero_level_info_v2_output import HeroLevelInfoV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of HeroLevelInfoV2Output from a JSON string
hero_level_info_v2_output_instance = HeroLevelInfoV2Output.from_json(json)
# print the JSON string representation of the object
print(HeroLevelInfoV2Output.to_json())

# convert the object into a dict
hero_level_info_v2_output_dict = hero_level_info_v2_output_instance.to_dict()
# create an instance of HeroLevelInfoV2Output from a dict
hero_level_info_v2_output_from_dict = HeroLevelInfoV2Output.from_dict(hero_level_info_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


