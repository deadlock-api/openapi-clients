# UpgradeTooltipSectionV2Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section_type** | [**RawAbilitySectionTypeV2**](RawAbilitySectionTypeV2.md) |  | [optional] 
**section_attributes** | [**List[UpgradeTooltipSectionAttributeV2]**](UpgradeTooltipSectionAttributeV2.md) |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.upgrade_tooltip_section_v2_output import UpgradeTooltipSectionV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeTooltipSectionV2Output from a JSON string
upgrade_tooltip_section_v2_output_instance = UpgradeTooltipSectionV2Output.from_json(json)
# print the JSON string representation of the object
print(UpgradeTooltipSectionV2Output.to_json())

# convert the object into a dict
upgrade_tooltip_section_v2_output_dict = upgrade_tooltip_section_v2_output_instance.to_dict()
# create an instance of UpgradeTooltipSectionV2Output from a dict
upgrade_tooltip_section_v2_output_from_dict = UpgradeTooltipSectionV2Output.from_dict(upgrade_tooltip_section_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


