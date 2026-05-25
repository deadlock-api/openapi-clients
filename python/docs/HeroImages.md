# HeroImages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_image** | **str** |  | [optional] 
**background_image_webp** | **str** |  | [optional] 
**hero_card_critical** | **str** |  | [optional] 
**hero_card_critical_webp** | **str** |  | [optional] 
**hero_card_gloat** | **str** |  | [optional] 
**hero_card_gloat_webp** | **str** |  | [optional] 
**icon_hero_card** | **str** |  | [optional] 
**icon_hero_card_webp** | **str** |  | [optional] 
**icon_image_small** | **str** |  | [optional] 
**icon_image_small_webp** | **str** |  | [optional] 
**minimap_image** | **str** |  | [optional] 
**minimap_image_webp** | **str** |  | [optional] 
**name_image** | **str** |  | [optional] 
**top_bar_vertical_image** | **str** |  | [optional] 
**top_bar_vertical_image_webp** | **str** |  | [optional] 
**weapon_image** | **str** |  | [optional] 
**weapon_image_webp** | **str** |  | [optional] 

## Example

```python
from deadlock_api_client.models.hero_images import HeroImages

# TODO update the JSON string below
json = "{}"
# create an instance of HeroImages from a JSON string
hero_images_instance = HeroImages.from_json(json)
# print the JSON string representation of the object
print(HeroImages.to_json())

# convert the object into a dict
hero_images_dict = hero_images_instance.to_dict()
# create an instance of HeroImages from a dict
hero_images_from_dict = HeroImages.from_dict(hero_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


