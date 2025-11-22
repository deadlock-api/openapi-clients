# LaneInfoV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lane_name** | **str** |  | 
**css_class** | **str** |  | [optional] 
**color** | [**ColorV1**](ColorV1.md) |  | 
**minimap_zipline_color_override** | [**ColorV1**](ColorV1.md) |  | [optional] 
**objective_color** | [**ColorV1**](ColorV1.md) |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.lane_info_v2 import LaneInfoV2

# TODO update the JSON string below
json = "{}"
# create an instance of LaneInfoV2 from a JSON string
lane_info_v2_instance = LaneInfoV2.from_json(json)
# print the JSON string representation of the object
print(LaneInfoV2.to_json())

# convert the object into a dict
lane_info_v2_dict = lane_info_v2_instance.to_dict()
# create an instance of LaneInfoV2 from a dict
lane_info_v2_from_dict = LaneInfoV2.from_dict(lane_info_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


