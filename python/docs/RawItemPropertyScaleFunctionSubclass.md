# RawItemPropertyScaleFunctionSubclass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | [optional] 
**scaling_stats** | **List[str]** |  | [optional] 
**specific_stat_scale_type** | **str** |  | [optional] 
**stat_scale** | **float** |  | [optional] 
**street_brawl_stat_scale** | **float** |  | [optional] 
**subclass_name** | **str** |  | [optional] 

## Example

```python
from deadlock_api_client.models.raw_item_property_scale_function_subclass import RawItemPropertyScaleFunctionSubclass

# TODO update the JSON string below
json = "{}"
# create an instance of RawItemPropertyScaleFunctionSubclass from a JSON string
raw_item_property_scale_function_subclass_instance = RawItemPropertyScaleFunctionSubclass.from_json(json)
# print the JSON string representation of the object
print(RawItemPropertyScaleFunctionSubclass.to_json())

# convert the object into a dict
raw_item_property_scale_function_subclass_dict = raw_item_property_scale_function_subclass_instance.to_dict()
# create an instance of RawItemPropertyScaleFunctionSubclass from a dict
raw_item_property_scale_function_subclass_from_dict = RawItemPropertyScaleFunctionSubclass.from_dict(raw_item_property_scale_function_subclass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


