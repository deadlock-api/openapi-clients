# LaneInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**Color**](Color.md) | Absent for unused lane slots (build 6711+). | [optional] 
**css_class** | **str** |  | [optional] 
**is_enemy_lane** | **bool** |  | 
**lane_name** | **str** | Localized lane name. Unused lane slots are named &#x60;Unused&#x60;. | 
**minimap_color** | [**Color**](Color.md) | Build 6711+. | [optional] 
**minimap_zipline_color_override** | [**Color**](Color.md) | Only present up to build 6701. | [optional] 
**objective_color** | [**Color**](Color.md) | Only present up to build 6701. | [optional] 

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


