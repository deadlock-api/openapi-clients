# MapImages

Fixed CDN URLs for the minimap image layers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | **str** |  | 
**frame** | **str** |  | 
**mid** | **str** |  | 
**minimap** | **str** |  | 
**plain** | **str** |  | 

## Example

```python
from deadlock_api_client.models.map_images import MapImages

# TODO update the JSON string below
json = "{}"
# create an instance of MapImages from a JSON string
map_images_instance = MapImages.from_json(json)
# print the JSON string representation of the object
print(MapImages.to_json())

# convert the object into a dict
map_images_dict = map_images_instance.to_dict()
# create an instance of MapImages from a dict
map_images_from_dict = MapImages.from_dict(map_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


