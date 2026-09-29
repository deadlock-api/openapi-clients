# FlashData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brightness** | **float** |  | [optional] 
**brightness_in_light_sensitivity_mode** | **float** |  | [optional] 
**color** | [**Color**](Color.md) | Flat flash color. From build 6711 on it is derived from the first &#x60;color_gradient&#x60; stop. | 
**color_gradient** | [**List[ColorGradientStop]**](ColorGradientStop.md) | Color gradient over the flash&#39;s lifetime (build 6711+). | [optional] 
**coverage** | **float** | Only present up to build 6701. | [optional] 
**duration** | **float** |  | 
**hardness** | **float** | Only present up to build 6701. | [optional] 

## Example

```python
from deadlock_api_client.models.flash_data import FlashData

# TODO update the JSON string below
json = "{}"
# create an instance of FlashData from a JSON string
flash_data_instance = FlashData.from_json(json)
# print the JSON string representation of the object
print(FlashData.to_json())

# convert the object into a dict
flash_data_dict = flash_data_instance.to_dict()
# create an instance of FlashData from a dict
flash_data_from_dict = FlashData.from_dict(flash_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


