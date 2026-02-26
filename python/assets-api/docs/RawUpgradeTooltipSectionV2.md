# RawUpgradeTooltipSectionV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section_type** | [**RawAbilitySectionTypeV2**](RawAbilitySectionTypeV2.md) |  | [optional] 
**section_attributes** | [**List[RawUpgradeTooltipSectionAttributeV2]**](RawUpgradeTooltipSectionAttributeV2.md) |  | 

## Example

```python
from assets_deadlock_api_client.models.raw_upgrade_tooltip_section_v2 import RawUpgradeTooltipSectionV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawUpgradeTooltipSectionV2 from a JSON string
raw_upgrade_tooltip_section_v2_instance = RawUpgradeTooltipSectionV2.from_json(json)
# print the JSON string representation of the object
print(RawUpgradeTooltipSectionV2.to_json())

# convert the object into a dict
raw_upgrade_tooltip_section_v2_dict = raw_upgrade_tooltip_section_v2_instance.to_dict()
# create an instance of RawUpgradeTooltipSectionV2 from a dict
raw_upgrade_tooltip_section_v2_from_dict = RawUpgradeTooltipSectionV2.from_dict(raw_upgrade_tooltip_section_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


