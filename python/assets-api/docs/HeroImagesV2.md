# HeroImagesV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon_hero_card** | **str** |  | [optional] 
**icon_hero_card_webp** | **str** |  | [optional] 
**icon_image_small** | **str** |  | [optional] 
**icon_image_small_webp** | **str** |  | [optional] 
**minimap_image** | **str** |  | [optional] 
**minimap_image_webp** | **str** |  | [optional] 
**selection_image** | **str** |  | [optional] 
**selection_image_webp** | **str** |  | [optional] 
**top_bar_image** | **str** |  | [optional] 
**top_bar_image_webp** | **str** |  | [optional] 
**top_bar_vertical_image** | **str** |  | [optional] 
**top_bar_vertical_image_webp** | **str** |  | [optional] 
**weapon_image** | **str** |  | [optional] 
**weapon_image_webp** | **str** |  | [optional] 
**background_image** | **str** |  | [optional] 
**background_image_webp** | **str** |  | [optional] 
**name_image** | **str** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.hero_images_v2 import HeroImagesV2

# TODO update the JSON string below
json = "{}"
# create an instance of HeroImagesV2 from a JSON string
hero_images_v2_instance = HeroImagesV2.from_json(json)
# print the JSON string representation of the object
print(HeroImagesV2.to_json())

# convert the object into a dict
hero_images_v2_dict = hero_images_v2_instance.to_dict()
# create an instance of HeroImagesV2 from a dict
hero_images_v2_from_dict = HeroImagesV2.from_dict(hero_images_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


