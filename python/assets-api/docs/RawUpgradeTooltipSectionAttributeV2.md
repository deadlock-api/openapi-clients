# RawUpgradeTooltipSectionAttributeV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc_string** | **str** |  | [optional] 
**properties** | **List[str]** |  | [optional] 
**elevated_properties** | **List[str]** |  | [optional] 
**important_properties** | [**List[RawUpgradeTooltipSectionAttributeImportantPropertyV2]**](RawUpgradeTooltipSectionAttributeImportantPropertyV2.md) |  | [optional] 
**important_properties_with_icon_path** | [**List[RawUpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon]**](RawUpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon.md) |  | 

## Example

```python
from assets_deadlock_api_client.models.raw_upgrade_tooltip_section_attribute_v2 import RawUpgradeTooltipSectionAttributeV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawUpgradeTooltipSectionAttributeV2 from a JSON string
raw_upgrade_tooltip_section_attribute_v2_instance = RawUpgradeTooltipSectionAttributeV2.from_json(json)
# print the JSON string representation of the object
print(RawUpgradeTooltipSectionAttributeV2.to_json())

# convert the object into a dict
raw_upgrade_tooltip_section_attribute_v2_dict = raw_upgrade_tooltip_section_attribute_v2_instance.to_dict()
# create an instance of RawUpgradeTooltipSectionAttributeV2 from a dict
raw_upgrade_tooltip_section_attribute_v2_from_dict = RawUpgradeTooltipSectionAttributeV2.from_dict(raw_upgrade_tooltip_section_attribute_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


