# BuildHeroDetailsCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**height** | **float** |  | [optional] 
**mods** | [**List[BuildHeroDetailsCategoryAbility]**](BuildHeroDetailsCategoryAbility.md) |  | [optional] 
**name** | **str** |  | 
**optional** | **bool** |  | [optional] 
**width** | **float** |  | [optional] 

## Example

```python
from deadlock_api_client.models.build_hero_details_category import BuildHeroDetailsCategory

# TODO update the JSON string below
json = "{}"
# create an instance of BuildHeroDetailsCategory from a JSON string
build_hero_details_category_instance = BuildHeroDetailsCategory.from_json(json)
# print the JSON string representation of the object
print(BuildHeroDetailsCategory.to_json())

# convert the object into a dict
build_hero_details_category_dict = build_hero_details_category_instance.to_dict()
# create an instance of BuildHeroDetailsCategory from a dict
build_hero_details_category_from_dict = BuildHeroDetailsCategory.from_dict(build_hero_details_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


