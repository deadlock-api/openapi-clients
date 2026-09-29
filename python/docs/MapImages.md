# MapImages

CDN URLs for the minimap image layers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | **str** | Background layer drawn under &#x60;mid&#x60;. Only for builds before 6711; the game no longer ships it, so it is omitted from build 6711 on. | [optional] 
**frame** | **str** |  | 
**mid** | **str** | Midtown base layer. | 
**mid_tunnels** | **str** | Mid tunnels overlay, drawn above &#x60;mid&#x60; (build 6711+). | [optional] 
**minimap** | **str** | Full minimap. From build 6711 on the game ships no composed minimap, so this is the same image as &#x60;mid&#x60;: the midtown street layer as a black mask on transparency, meant to be drawn over a base colour rather than shown on its own. | 
**plain** | **str** | Minimap without overlays. From build 6711 on this is the same street mask as &#x60;mid&#x60; (see &#x60;minimap&#x60;). | 
**rat_tunnels** | **str** | Rat tunnels overlay, drawn above &#x60;mid_tunnels&#x60; (build 6711+). | [optional] 

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


