# ZiplanePath

A single lane's zip-line cubic spline.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**p0_points** | **List[List[float]]** |  | 
**p1_points** | **List[List[float]]** |  | 
**p2_points** | **List[List[float]]** |  | 
**color** | **str** |  | 
**color_parsed** | [**Color**](Color.md) |  | 
**origin** | **List[float]** |  | 

## Example

```python
from deadlock_api_client.models.ziplane_path import ZiplanePath

# TODO update the JSON string below
json = "{}"
# create an instance of ZiplanePath from a JSON string
ziplane_path_instance = ZiplanePath.from_json(json)
# print the JSON string representation of the object
print(ZiplanePath.to_json())

# convert the object into a dict
ziplane_path_dict = ziplane_path_instance.to_dict()
# create an instance of ZiplanePath from a dict
ziplane_path_from_dict = ZiplanePath.from_dict(ziplane_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


