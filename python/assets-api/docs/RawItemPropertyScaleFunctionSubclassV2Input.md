# RawItemPropertyScaleFunctionSubclassV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | **str** |  | [optional] 
**my_subclass_name** | **str** |  | [optional] 
**m_e_specific_stat_scale_type** | **str** |  | [optional] 
**m_vec_scaling_stats** | **List[str]** |  | [optional] 
**m_fl_stat_scale** | **float** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.raw_item_property_scale_function_subclass_v2_input import RawItemPropertyScaleFunctionSubclassV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of RawItemPropertyScaleFunctionSubclassV2Input from a JSON string
raw_item_property_scale_function_subclass_v2_input_instance = RawItemPropertyScaleFunctionSubclassV2Input.from_json(json)
# print the JSON string representation of the object
print(RawItemPropertyScaleFunctionSubclassV2Input.to_json())

# convert the object into a dict
raw_item_property_scale_function_subclass_v2_input_dict = raw_item_property_scale_function_subclass_v2_input_instance.to_dict()
# create an instance of RawItemPropertyScaleFunctionSubclassV2Input from a dict
raw_item_property_scale_function_subclass_v2_input_from_dict = RawItemPropertyScaleFunctionSubclassV2Input.from_dict(raw_item_property_scale_function_subclass_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


