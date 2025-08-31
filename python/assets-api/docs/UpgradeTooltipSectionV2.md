# UpgradeTooltipSectionV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section_type** | [**RawAbilitySectionTypeV2**](RawAbilitySectionTypeV2.md) |  | [optional] 
**section_attributes** | [**List[UpgradeTooltipSectionAttributeV2]**](UpgradeTooltipSectionAttributeV2.md) |  | [optional] 

## Example

```python
from openapi_client.models.upgrade_tooltip_section_v2 import UpgradeTooltipSectionV2

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeTooltipSectionV2 from a JSON string
upgrade_tooltip_section_v2_instance = UpgradeTooltipSectionV2.from_json(json)
# print the JSON string representation of the object
print(UpgradeTooltipSectionV2.to_json())

# convert the object into a dict
upgrade_tooltip_section_v2_dict = upgrade_tooltip_section_v2_instance.to_dict()
# create an instance of UpgradeTooltipSectionV2 from a dict
upgrade_tooltip_section_v2_from_dict = UpgradeTooltipSectionV2.from_dict(upgrade_tooltip_section_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


