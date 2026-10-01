# MapEntity

An interactable map entity (crate, bounce pad, shop, ...). Deserialized from `map/entities.json`, which has no minimap position; that is filled in after.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Variant within the category, e.g. &#x60;wooden_crate&#x60; or &#x60;secret&#x60; (shops). | [optional] 
**left_relative** | **float** | Position on the minimap, as fractions of its width/height. | [optional] 
**position** | **List[float]** | World position &#x60;[x, y, z]&#x60;, same space as the zip-line splines. Brush triggers (ropes, pads, veils, ...) are placed at their entity origin. | 
**target** | **List[float]** | World position &#x60;[x, y, z]&#x60; the entity sends you to: the teleporter exit or the bounce pad landing spot. | [optional] 
**team** | **int** | Owning team (0 or 1); absent for neutral entities. | [optional] 
**top_relative** | **float** |  | [optional] 

## Example

```python
from deadlock_api_client.models.map_entity import MapEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MapEntity from a JSON string
map_entity_instance = MapEntity.from_json(json)
# print the JSON string representation of the object
print(MapEntity.to_json())

# convert the object into a dict
map_entity_dict = map_entity_instance.to_dict()
# create an instance of MapEntity from a dict
map_entity_from_dict = MapEntity.from_dict(map_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


