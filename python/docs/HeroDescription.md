# HeroDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lore** | **str** |  | [optional] 
**playstyle** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from deadlock_api_client.models.hero_description import HeroDescription

# TODO update the JSON string below
json = "{}"
# create an instance of HeroDescription from a JSON string
hero_description_instance = HeroDescription.from_json(json)
# print the JSON string representation of the object
print(HeroDescription.to_json())

# convert the object into a dict
hero_description_dict = hero_description_instance.to_dict()
# create an instance of HeroDescription from a dict
hero_description_from_dict = HeroDescription.from_dict(hero_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


