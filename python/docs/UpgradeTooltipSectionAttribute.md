# UpgradeTooltipSectionAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elevated_properties** | **List[str]** |  | [optional] 
**important_properties** | **List[str]** |  | [optional] 
**important_properties_with_icon** | [**List[UpgradeTooltipImportantPropertyWithIcon]**](UpgradeTooltipImportantPropertyWithIcon.md) |  | [optional] 
**loc_string** | **str** |  | [optional] 
**properties** | **List[str]** |  | [optional] 

## Example

```python
from deadlock_api_client.models.upgrade_tooltip_section_attribute import UpgradeTooltipSectionAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeTooltipSectionAttribute from a JSON string
upgrade_tooltip_section_attribute_instance = UpgradeTooltipSectionAttribute.from_json(json)
# print the JSON string representation of the object
print(UpgradeTooltipSectionAttribute.to_json())

# convert the object into a dict
upgrade_tooltip_section_attribute_dict = upgrade_tooltip_section_attribute_instance.to_dict()
# create an instance of UpgradeTooltipSectionAttribute from a dict
upgrade_tooltip_section_attribute_from_dict = UpgradeTooltipSectionAttribute.from_dict(upgrade_tooltip_section_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


