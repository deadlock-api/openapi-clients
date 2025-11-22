# MiniMapOffsets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_class** | **str** |  | 
**offset_2d** | **List[float]** |  | 
**lane_index** | **int** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.mini_map_offsets import MiniMapOffsets

# TODO update the JSON string below
json = "{}"
# create an instance of MiniMapOffsets from a JSON string
mini_map_offsets_instance = MiniMapOffsets.from_json(json)
# print the JSON string representation of the object
print(MiniMapOffsets.to_json())

# convert the object into a dict
mini_map_offsets_dict = mini_map_offsets_instance.to_dict()
# create an instance of MiniMapOffsets from a dict
mini_map_offsets_from_dict = MiniMapOffsets.from_dict(mini_map_offsets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


