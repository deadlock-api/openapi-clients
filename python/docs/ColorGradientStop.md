# ColorGradientStop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**Color**](Color.md) |  | 
**position** | **float** | Position of the stop along the flash&#39;s lifetime, &#x60;0.0..&#x3D;1.0&#x60;. | 

## Example

```python
from deadlock_api_client.models.color_gradient_stop import ColorGradientStop

# TODO update the JSON string below
json = "{}"
# create an instance of ColorGradientStop from a JSON string
color_gradient_stop_instance = ColorGradientStop.from_json(json)
# print the JSON string representation of the object
print(ColorGradientStop.to_json())

# convert the object into a dict
color_gradient_stop_dict = color_gradient_stop_instance.to_dict()
# create an instance of ColorGradientStop from a dict
color_gradient_stop_from_dict = ColorGradientStop.from_dict(color_gradient_stop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


