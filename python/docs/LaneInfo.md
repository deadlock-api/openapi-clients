# LaneInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**Color**](Color.md) |  | 
**css_class** | **str** |  | [optional] 
**lane_name** | **str** |  | 
**minimap_zipline_color_override** | [**Color**](Color.md) |  | [optional] 
**objective_color** | [**Color**](Color.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.lane_info import LaneInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LaneInfo from a JSON string
lane_info_instance = LaneInfo.from_json(json)
# print the JSON string representation of the object
print(LaneInfo.to_json())

# convert the object into a dict
lane_info_dict = lane_info_instance.to_dict()
# create an instance of LaneInfo from a dict
lane_info_from_dict = LaneInfo.from_dict(lane_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


