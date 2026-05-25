# UpgradeTooltipSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section_attributes** | [**List[UpgradeTooltipSectionAttribute]**](UpgradeTooltipSectionAttribute.md) |  | [optional] 
**section_type** | [**AbilitySectionType**](AbilitySectionType.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.upgrade_tooltip_section import UpgradeTooltipSection

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeTooltipSection from a JSON string
upgrade_tooltip_section_instance = UpgradeTooltipSection.from_json(json)
# print the JSON string representation of the object
print(UpgradeTooltipSection.to_json())

# convert the object into a dict
upgrade_tooltip_section_dict = upgrade_tooltip_section_instance.to_dict()
# create an instance of UpgradeTooltipSection from a dict
upgrade_tooltip_section_from_dict = UpgradeTooltipSection.from_dict(upgrade_tooltip_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


