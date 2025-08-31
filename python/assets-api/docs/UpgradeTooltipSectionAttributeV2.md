# UpgradeTooltipSectionAttributeV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc_string** | **str** |  | [optional] 
**properties** | **List[str]** |  | [optional] 
**elevated_properties** | **List[str]** |  | [optional] 
**important_properties** | **List[str]** |  | [optional] 
**important_properties_with_icon** | [**List[UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon]**](UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon.md) |  | [optional] 

## Example

```python
from openapi_client.models.upgrade_tooltip_section_attribute_v2 import UpgradeTooltipSectionAttributeV2

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeTooltipSectionAttributeV2 from a JSON string
upgrade_tooltip_section_attribute_v2_instance = UpgradeTooltipSectionAttributeV2.from_json(json)
# print the JSON string representation of the object
print(UpgradeTooltipSectionAttributeV2.to_json())

# convert the object into a dict
upgrade_tooltip_section_attribute_v2_dict = upgrade_tooltip_section_attribute_v2_instance.to_dict()
# create an instance of UpgradeTooltipSectionAttributeV2 from a dict
upgrade_tooltip_section_attribute_v2_from_dict = UpgradeTooltipSectionAttributeV2.from_dict(upgrade_tooltip_section_attribute_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


