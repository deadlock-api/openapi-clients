# ItemPropertyV2Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**Value1**](Value1.md) |  | [optional] 
**can_set_token_override** | **bool** |  | [optional] 
**provided_property_type** | **str** |  | [optional] 
**css_class** | **str** |  | [optional] 
**usage_flags** | [**UsageFlags**](UsageFlags.md) |  | [optional] 
**negative_attribute** | **bool** |  | [optional] 
**disable_value** | **str** |  | [optional] 
**loc_token_override** | **str** |  | [optional] 
**display_units** | **str** |  | [optional] 
**icon_path** | **str** |  | [optional] 
**scale_function** | [**RawItemPropertyScaleFunctionSubclassV2Output**](RawItemPropertyScaleFunctionSubclassV2Output.md) |  | [optional] 
**prefix** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**postfix** | **str** |  | [optional] 
**postvalue_label** | **str** |  | [optional] 
**conditional** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.item_property_v2_output import ItemPropertyV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPropertyV2Output from a JSON string
item_property_v2_output_instance = ItemPropertyV2Output.from_json(json)
# print the JSON string representation of the object
print(ItemPropertyV2Output.to_json())

# convert the object into a dict
item_property_v2_output_dict = item_property_v2_output_instance.to_dict()
# create an instance of ItemPropertyV2Output from a dict
item_property_v2_output_from_dict = ItemPropertyV2Output.from_dict(item_property_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


