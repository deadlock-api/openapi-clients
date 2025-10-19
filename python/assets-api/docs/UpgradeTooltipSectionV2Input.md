# UpgradeTooltipSectionV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section_type** | [**RawAbilitySectionTypeV2**](RawAbilitySectionTypeV2.md) |  | [optional] 
**section_attributes** | [**List[UpgradeTooltipSectionAttributeV2]**](UpgradeTooltipSectionAttributeV2.md) |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.upgrade_tooltip_section_v2_input import UpgradeTooltipSectionV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeTooltipSectionV2Input from a JSON string
upgrade_tooltip_section_v2_input_instance = UpgradeTooltipSectionV2Input.from_json(json)
# print the JSON string representation of the object
print(UpgradeTooltipSectionV2Input.to_json())

# convert the object into a dict
upgrade_tooltip_section_v2_input_dict = upgrade_tooltip_section_v2_input_instance.to_dict()
# create an instance of UpgradeTooltipSectionV2Input from a dict
upgrade_tooltip_section_v2_input_from_dict = UpgradeTooltipSectionV2Input.from_dict(upgrade_tooltip_section_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


