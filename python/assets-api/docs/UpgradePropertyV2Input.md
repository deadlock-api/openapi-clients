# UpgradePropertyV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_str_value** | [**MStrvalue**](MStrvalue.md) |  | [optional] 
**m_b_can_set_token_override** | **bool** |  | [optional] 
**m_e_provided_property_type** | **str** |  | [optional] 
**m_str_css_class** | **str** |  | [optional] 
**m_e_stats_usage_flags** | [**MEstatsusageflags**](MEstatsusageflags.md) |  | [optional] 
**m_b_is_negative_attribute** | **bool** |  | [optional] 
**m_str_disable_value** | **str** |  | [optional] 
**m_str_loc_token_override** | **str** |  | [optional] 
**m_e_display_units** | **str** |  | [optional] 
**scale_function** | [**RawItemPropertyScaleFunctionSubclassV2Input**](RawItemPropertyScaleFunctionSubclassV2Input.md) |  | [optional] 
**prefix** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**postfix** | **str** |  | [optional] 
**postvalue_label** | **str** |  | [optional] 
**conditional** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**tooltip_section** | [**RawAbilitySectionTypeV2**](RawAbilitySectionTypeV2.md) |  | [optional] 
**tooltip_is_elevated** | **bool** |  | [optional] 
**tooltip_is_important** | **bool** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.upgrade_property_v2_input import UpgradePropertyV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradePropertyV2Input from a JSON string
upgrade_property_v2_input_instance = UpgradePropertyV2Input.from_json(json)
# print the JSON string representation of the object
print(UpgradePropertyV2Input.to_json())

# convert the object into a dict
upgrade_property_v2_input_dict = upgrade_property_v2_input_instance.to_dict()
# create an instance of UpgradePropertyV2Input from a dict
upgrade_property_v2_input_from_dict = UpgradePropertyV2Input.from_dict(upgrade_property_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


