# Viewport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_pixel_ratio** | **float** |  | 
**height** | **int** |  | 
**width** | **int** |  | 

## Example

```python
from deadlock_api_client.models.viewport import Viewport

# TODO update the JSON string below
json = "{}"
# create an instance of Viewport from a JSON string
viewport_instance = Viewport.from_json(json)
# print the JSON string representation of the object
print(Viewport.to_json())

# convert the object into a dict
viewport_dict = viewport_instance.to_dict()
# create an instance of Viewport from a dict
viewport_from_dict = Viewport.from_dict(viewport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


