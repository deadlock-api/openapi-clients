# ItemOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | 
**crosshair_css_class** | **str** |  | [optional] 
**custom_crosshair_settings** | [**RawCustomCrosshairSettings**](RawCustomCrosshairSettings.md) |  | [optional] 
**hero** | **int** |  | [optional] 
**heroes** | **List[int]** |  | [optional] 
**id** | **int** |  | 
**image** | **str** |  | [optional] 
**image_webp** | **str** |  | [optional] 
**name** | **str** |  | 
**properties** | [**Dict[str, ItemProperty]**](ItemProperty.md) |  | [optional] 
**start_trained** | **bool** |  | [optional] 
**update_time** | **int** |  | [optional] 
**use_custom_crosshair_settings** | **bool** |  | [optional] 
**weapon_info** | [**WeaponInfo**](WeaponInfo.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from deadlock_api_client.models.item_one_of1 import ItemOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ItemOneOf1 from a JSON string
item_one_of1_instance = ItemOneOf1.from_json(json)
# print the JSON string representation of the object
print(ItemOneOf1.to_json())

# convert the object into a dict
item_one_of1_dict = item_one_of1_instance.to_dict()
# create an instance of ItemOneOf1 from a dict
item_one_of1_from_dict = ItemOneOf1.from_dict(item_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


