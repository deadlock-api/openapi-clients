# MapImagesV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimap** | **str** | The minimap image of the map. | 
**plain** | **str** | The minimap image of the map without background image and frame image. | 
**background** | **str** | The background image of the map. | 
**frame** | **str** | The frame image of the map. | 
**mid** | **str** | The mid image of the map. | 

## Example

```python
from openapi_client.models.map_images_v1 import MapImagesV1

# TODO update the JSON string below
json = "{}"
# create an instance of MapImagesV1 from a JSON string
map_images_v1_instance = MapImagesV1.from_json(json)
# print the JSON string representation of the object
print(MapImagesV1.to_json())

# convert the object into a dict
map_images_v1_dict = map_images_v1_instance.to_dict()
# create an instance of MapImagesV1 from a dict
map_images_v1_from_dict = MapImagesV1.from_dict(map_images_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


