# BuildHeroDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ability_order** | [**BuildHeroDetailsAbilityOrder**](BuildHeroDetailsAbilityOrder.md) |  | [optional] 
**mod_categories** | [**List[BuildHeroDetailsCategory]**](BuildHeroDetailsCategory.md) |  | 

## Example

```python
from deadlock_api_client.models.build_hero_details import BuildHeroDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BuildHeroDetails from a JSON string
build_hero_details_instance = BuildHeroDetails.from_json(json)
# print the JSON string representation of the object
print(BuildHeroDetails.to_json())

# convert the object into a dict
build_hero_details_dict = build_hero_details_instance.to_dict()
# create an instance of BuildHeroDetails from a dict
build_hero_details_from_dict = BuildHeroDetails.from_dict(build_hero_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


