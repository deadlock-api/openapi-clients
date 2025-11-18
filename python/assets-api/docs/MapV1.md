# MapV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**radius** | **int** | The radius of the map. | [optional] [default to 10752]
**images** | [**MapImagesV1**](MapImagesV1.md) | The images of the map. | 
**objective_positions** | [**ObjectivePositionsV1**](ObjectivePositionsV1.md) |  | [readonly] 
**zipline_paths** | [**List[ZiplanePathV1]**](ZiplanePathV1.md) | The ziplane paths of the map. Each path is a list of P0, P1, and P2 points, describing the cubic spline. | 

## Example

```python
from assets_deadlock_api_client.models.map_v1 import MapV1

# TODO update the JSON string below
json = "{}"
# create an instance of MapV1 from a JSON string
map_v1_instance = MapV1.from_json(json)
# print the JSON string representation of the object
print(MapV1.to_json())

# convert the object into a dict
map_v1_dict = map_v1_instance.to_dict()
# create an instance of MapV1 from a dict
map_v1_from_dict = MapV1.from_dict(map_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


