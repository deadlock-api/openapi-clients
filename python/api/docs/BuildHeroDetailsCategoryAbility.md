# BuildHeroDetailsCategoryAbility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ability_id** | **int** |  | 
**annotation** | **str** |  | [optional] 
**imbue_target_ability_id** | **int** |  | [optional] 
**required_flex_slots** | **int** |  | [optional] 
**sell_priority** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.build_hero_details_category_ability import BuildHeroDetailsCategoryAbility

# TODO update the JSON string below
json = "{}"
# create an instance of BuildHeroDetailsCategoryAbility from a JSON string
build_hero_details_category_ability_instance = BuildHeroDetailsCategoryAbility.from_json(json)
# print the JSON string representation of the object
print(BuildHeroDetailsCategoryAbility.to_json())

# convert the object into a dict
build_hero_details_category_ability_dict = build_hero_details_category_ability_instance.to_dict()
# create an instance of BuildHeroDetailsCategoryAbility from a dict
build_hero_details_category_ability_from_dict = BuildHeroDetailsCategoryAbility.from_dict(build_hero_details_category_ability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


