# GlitchSettingsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strength** | **float** |  | 
**uantize_type** | **float** |  | 
**quantize_scale** | **float** |  | 
**quantize_strength** | **float** |  | 
**frame_rate** | **float** |  | 
**speed** | **float** |  | 
**jump_strength** | **float** |  | 
**distort_strength** | **float** |  | 
**white_noise_strength** | **float** |  | 
**scanline_strength** | **float** |  | 
**breakup_strength** | **float** |  | 

## Example

```python
from assets_deadlock_api_client.models.glitch_settings_v2 import GlitchSettingsV2

# TODO update the JSON string below
json = "{}"
# create an instance of GlitchSettingsV2 from a JSON string
glitch_settings_v2_instance = GlitchSettingsV2.from_json(json)
# print the JSON string representation of the object
print(GlitchSettingsV2.to_json())

# convert the object into a dict
glitch_settings_v2_dict = glitch_settings_v2_instance.to_dict()
# create an instance of GlitchSettingsV2 from a dict
glitch_settings_v2_from_dict = GlitchSettingsV2.from_dict(glitch_settings_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


