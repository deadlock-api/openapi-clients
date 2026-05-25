# FlashData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brightness** | **float** |  | 
**brightness_in_light_sensitivity_mode** | **float** |  | [optional] 
**color** | [**Color**](Color.md) |  | 
**coverage** | **float** |  | 
**duration** | **float** |  | 
**hardness** | **float** |  | 

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


