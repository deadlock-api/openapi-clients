# Settings

Crosshair convars. Anything not given keeps the game's default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color_b** | **int** |  | [optional] [default to 255]
**color_g** | **int** |  | [optional] [default to 255]
**color_r** | **int** |  | [optional] [default to 255]
**dot_opacity** | **float** | 0 to 1. | [optional] [default to 0.7]
**dot_outline_border** | **int** |  | [optional] [default to 2]
**dot_outline_gap** | **int** |  | [optional] [default to 0]
**dot_outline_opacity** | **float** | 0 to 1. | [optional] [default to 0.7]
**dot_size** | **int** |  | [optional] [default to 4]
**outline_color_b** | **int** |  | [optional] [default to 0]
**outline_color_g** | **int** |  | [optional] [default to 0]
**outline_color_r** | **int** |  | [optional] [default to 0]
**pip_gap** | **int** |  | [optional] [default to 4]
**pip_gap_static** | **bool** | Keep the pips at a fixed distance instead of spreading them with weapon spread. | [optional] [default to False]
**pip_height** | **int** |  | [optional] [default to 16]
**pip_opacity** | **float** | 0 to 1. | [optional] [default to 0.5]
**pip_outline_border** | **int** |  | [optional] [default to 1]
**pip_outline_gap** | **int** |  | [optional] [default to 0]
**pip_outline_opacity** | **float** | 0 to 1. | [optional] [default to 0.7]
**pip_width** | **int** |  | [optional] [default to 2]
**themed** | **bool** | Use the hero&#39;s own crosshair instead of these settings. | [optional] [default to False]

## Example

```python
from deadlock_api_client.models.settings import Settings

# TODO update the JSON string below
json = "{}"
# create an instance of Settings from a JSON string
settings_instance = Settings.from_json(json)
# print the JSON string representation of the object
print(Settings.to_json())

# convert the object into a dict
settings_dict = settings_instance.to_dict()
# create an instance of Settings from a dict
settings_from_dict = Settings.from_dict(settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


