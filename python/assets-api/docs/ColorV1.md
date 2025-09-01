# ColorV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**red** | **int** | The red value of the color. | 
**green** | **int** | The green value of the color. | 
**blue** | **int** | The blue value of the color. | 
**alpha** | **int** | The alpha value of the color. | 

## Example

```python
from assets-deadlock-api-client.models.color_v1 import ColorV1

# TODO update the JSON string below
json = "{}"
# create an instance of ColorV1 from a JSON string
color_v1_instance = ColorV1.from_json(json)
# print the JSON string representation of the object
print(ColorV1.to_json())

# convert the object into a dict
color_v1_dict = color_v1_instance.to_dict()
# create an instance of ColorV1 from a dict
color_v1_from_dict = ColorV1.from_dict(color_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


