# RawItemPropertyV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**Value1**](Value1.md) |  | [optional] 
**street_brawl_value** | [**StreetBrawlValue**](StreetBrawlValue.md) |  | [optional] 
**can_set_token_override** | **bool** |  | [optional] 
**provided_property_type** | **str** |  | [optional] 
**css_class** | **str** |  | [optional] 
**usage_flags** | [**UsageFlags**](UsageFlags.md) |  | [optional] 
**negative_attribute** | **bool** |  | [optional] 
**disable_value** | **str** |  | [optional] 
**loc_token_override** | **str** |  | [optional] 
**display_units** | **str** |  | [optional] 
**icon_path** | **str** |  | [optional] 
**scale_function** | [**RawItemPropertyScaleFunctionV2**](RawItemPropertyScaleFunctionV2.md) |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.raw_item_property_v2 import RawItemPropertyV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawItemPropertyV2 from a JSON string
raw_item_property_v2_instance = RawItemPropertyV2.from_json(json)
# print the JSON string representation of the object
print(RawItemPropertyV2.to_json())

# convert the object into a dict
raw_item_property_v2_dict = raw_item_property_v2_instance.to_dict()
# create an instance of RawItemPropertyV2 from a dict
raw_item_property_v2_from_dict = RawItemPropertyV2.from_dict(raw_item_property_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


