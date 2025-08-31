# HeroDescriptionV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lore** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**playstyle** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.hero_description_v2 import HeroDescriptionV2

# TODO update the JSON string below
json = "{}"
# create an instance of HeroDescriptionV2 from a JSON string
hero_description_v2_instance = HeroDescriptionV2.from_json(json)
# print the JSON string representation of the object
print(HeroDescriptionV2.to_json())

# convert the object into a dict
hero_description_v2_dict = hero_description_v2_instance.to_dict()
# create an instance of HeroDescriptionV2 from a dict
hero_description_v2_from_dict = HeroDescriptionV2.from_dict(hero_description_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


