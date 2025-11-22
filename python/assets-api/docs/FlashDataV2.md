# FlashDataV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **float** |  | 
**coverage** | **float** |  | 
**hardness** | **float** |  | 
**brightness** | **float** |  | 
**color** | [**ColorV1**](ColorV1.md) |  | 
**brightness_in_light_sensitivity_mode** | **float** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.flash_data_v2 import FlashDataV2

# TODO update the JSON string below
json = "{}"
# create an instance of FlashDataV2 from a JSON string
flash_data_v2_instance = FlashDataV2.from_json(json)
# print the JSON string representation of the object
print(FlashDataV2.to_json())

# convert the object into a dict
flash_data_v2_dict = flash_data_v2_instance.to_dict()
# create an instance of FlashDataV2 from a dict
flash_data_v2_from_dict = FlashDataV2.from_dict(flash_data_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


