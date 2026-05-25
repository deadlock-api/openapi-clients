# GlitchSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakup_strength** | **float** |  | 
**distort_strength** | **float** |  | 
**frame_rate** | **float** |  | 
**jump_strength** | **float** |  | 
**quantize_scale** | **float** |  | 
**quantize_strength** | **float** |  | 
**scanline_strength** | **float** |  | 
**speed** | **float** |  | 
**strength** | **float** |  | 
**uantize_type** | **float** | Field name preserved as-is for &#x60;/v2/generic-data&#x60; compatibility. | 
**white_noise_strength** | **float** |  | 

## Example

```python
from deadlock_api_client.models.glitch_settings import GlitchSettings

# TODO update the JSON string below
json = "{}"
# create an instance of GlitchSettings from a JSON string
glitch_settings_instance = GlitchSettings.from_json(json)
# print the JSON string representation of the object
print(GlitchSettings.to_json())

# convert the object into a dict
glitch_settings_dict = glitch_settings_instance.to_dict()
# create an instance of GlitchSettings from a dict
glitch_settings_from_dict = GlitchSettings.from_dict(glitch_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


