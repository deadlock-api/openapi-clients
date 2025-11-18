# HeroColorsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**glow_enemy** | **List[object]** |  | 
**glow_friendly** | **List[object]** |  | 
**glow_team1** | **List[object]** |  | 
**glow_team2** | **List[object]** |  | 
**ui** | **List[object]** |  | 

## Example

```python
from assets_deadlock_api_client.models.hero_colors_v2 import HeroColorsV2

# TODO update the JSON string below
json = "{}"
# create an instance of HeroColorsV2 from a JSON string
hero_colors_v2_instance = HeroColorsV2.from_json(json)
# print the JSON string representation of the object
print(HeroColorsV2.to_json())

# convert the object into a dict
hero_colors_v2_dict = hero_colors_v2_instance.to_dict()
# create an instance of HeroColorsV2 from a dict
hero_colors_v2_from_dict = HeroColorsV2.from_dict(hero_colors_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


