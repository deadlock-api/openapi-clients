# RawCustomCrosshairSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_dot_color** | **List[int]** |  | [optional] 
**m_dot_outline_color** | **List[int]** |  | [optional] 
**m_pip_color** | **List[int]** |  | [optional] 
**m_pip_outline_color** | **List[int]** |  | [optional] 
**m_spread_indicating_element** | **str** |  | [optional] 
**m_fl_base_spread** | **float** |  | [optional] 
**m_fl_dot_opacity** | **float** |  | [optional] 
**m_fl_dot_outline_opacity** | **float** |  | [optional] 
**m_fl_pip_opacity** | **float** |  | [optional] 
**m_fl_pip_outline_opacity** | **float** |  | [optional] 
**m_n_dot_outline_gap** | **int** |  | [optional] 
**m_n_dot_outline_width** | **int** |  | [optional] 
**m_n_dot_radius** | **int** |  | [optional] 
**m_n_pip_height** | **int** |  | [optional] 
**m_n_pip_outline_gap** | **int** |  | [optional] 
**m_n_pip_outline_width** | **int** |  | [optional] 
**m_n_pip_width** | **int** |  | [optional] 

## Example

```python
from deadlock_api_client.models.raw_custom_crosshair_settings import RawCustomCrosshairSettings

# TODO update the JSON string below
json = "{}"
# create an instance of RawCustomCrosshairSettings from a JSON string
raw_custom_crosshair_settings_instance = RawCustomCrosshairSettings.from_json(json)
# print the JSON string representation of the object
print(RawCustomCrosshairSettings.to_json())

# convert the object into a dict
raw_custom_crosshair_settings_dict = raw_custom_crosshair_settings_instance.to_dict()
# create an instance of RawCustomCrosshairSettings from a dict
raw_custom_crosshair_settings_from_dict = RawCustomCrosshairSettings.from_dict(raw_custom_crosshair_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


