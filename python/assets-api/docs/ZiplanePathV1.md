# ZiplanePathV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin** | **List[object]** | The origin of the path. | 
**color** | **str** | The color of the path. | 
**p0_points** | **List[List[object]]** | The P0 points of the path. | 
**p1_points** | **List[List[object]]** | The P1 points of the path. | 
**p2_points** | **List[List[object]]** | The P2 points of the path. | 

## Example

```python
from assets_deadlock_api_client.models.ziplane_path_v1 import ZiplanePathV1

# TODO update the JSON string below
json = "{}"
# create an instance of ZiplanePathV1 from a JSON string
ziplane_path_v1_instance = ZiplanePathV1.from_json(json)
# print the JSON string representation of the object
print(ZiplanePathV1.to_json())

# convert the object into a dict
ziplane_path_v1_dict = ziplane_path_v1_instance.to_dict()
# create an instance of ZiplanePathV1 from a dict
ziplane_path_v1_from_dict = ZiplanePathV1.from_dict(ziplane_path_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


