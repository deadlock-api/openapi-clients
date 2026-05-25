# HeroColors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**style** | **List[int]** |  | [optional] 
**style_hex** | **str** |  | [optional] 
**ui** | **List[int]** |  | 

## Example

```python
from deadlock_api_client.models.hero_colors import HeroColors

# TODO update the JSON string below
json = "{}"
# create an instance of HeroColors from a JSON string
hero_colors_instance = HeroColors.from_json(json)
# print the JSON string representation of the object
print(HeroColors.to_json())

# convert the object into a dict
hero_colors_dict = hero_colors_instance.to_dict()
# create an instance of HeroColors from a dict
hero_colors_from_dict = HeroColors.from_dict(hero_colors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


