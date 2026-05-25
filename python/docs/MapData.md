# MapData

The `/v1/assets/map` response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | [**MapImages**](MapImages.md) |  | 
**objective_positions** | [**Dict[str, ObjectivePosition]**](ObjectivePosition.md) |  | 
**radius** | **int** |  | 
**zipline_paths** | [**List[ZiplanePath]**](ZiplanePath.md) |  | 

## Example

```python
from deadlock_api_client.models.map_data import MapData

# TODO update the JSON string below
json = "{}"
# create an instance of MapData from a JSON string
map_data_instance = MapData.from_json(json)
# print the JSON string representation of the object
print(MapData.to_json())

# convert the object into a dict
map_data_dict = map_data_instance.to_dict()
# create an instance of MapData from a dict
map_data_from_dict = MapData.from_dict(map_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


