# RawCustomCrosshairSettingsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pip_width** | **int** |  | [optional] 
**pip_height** | **int** |  | [optional] 
**pip_outline_width** | **int** |  | [optional] 
**pip_outline_gap** | **int** |  | [optional] 
**pip_opacity** | **float** |  | [optional] 
**pip_outline_opacity** | **float** |  | [optional] 
**pip_color** | **List[int]** |  | [optional] 
**pip_outline_color** | **List[int]** |  | [optional] 
**dot_radius** | **int** |  | [optional] 
**dot_outline_width** | **int** |  | [optional] 
**dot_outline_gap** | **int** |  | [optional] 
**dot_opacity** | **float** |  | [optional] 
**dot_outline_opacity** | **float** |  | [optional] 
**dot_color** | **List[int]** |  | [optional] 
**dot_outline_color** | **List[int]** |  | [optional] 
**spread_indicating_element** | **str** |  | [optional] 
**base_spread** | **float** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.raw_custom_crosshair_settings_v2 import RawCustomCrosshairSettingsV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawCustomCrosshairSettingsV2 from a JSON string
raw_custom_crosshair_settings_v2_instance = RawCustomCrosshairSettingsV2.from_json(json)
# print the JSON string representation of the object
print(RawCustomCrosshairSettingsV2.to_json())

# convert the object into a dict
raw_custom_crosshair_settings_v2_dict = raw_custom_crosshair_settings_v2_instance.to_dict()
# create an instance of RawCustomCrosshairSettingsV2 from a dict
raw_custom_crosshair_settings_v2_from_dict = RawCustomCrosshairSettingsV2.from_dict(raw_custom_crosshair_settings_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


