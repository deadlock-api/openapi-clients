# AbilityTooltipDetailsInfoSectionV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc_string** | **str** |  | [optional] 
**property_upgrade_required** | **str** |  | [optional] 
**properties_block** | [**List[AbilityTooltipDetailsInfoSectionPropertyBlockV2]**](AbilityTooltipDetailsInfoSectionPropertyBlockV2.md) |  | [optional] 
**basic_properties** | **List[str]** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.ability_tooltip_details_info_section_v2 import AbilityTooltipDetailsInfoSectionV2

# TODO update the JSON string below
json = "{}"
# create an instance of AbilityTooltipDetailsInfoSectionV2 from a JSON string
ability_tooltip_details_info_section_v2_instance = AbilityTooltipDetailsInfoSectionV2.from_json(json)
# print the JSON string representation of the object
print(AbilityTooltipDetailsInfoSectionV2.to_json())

# convert the object into a dict
ability_tooltip_details_info_section_v2_dict = ability_tooltip_details_info_section_v2_instance.to_dict()
# create an instance of AbilityTooltipDetailsInfoSectionV2 from a dict
ability_tooltip_details_info_section_v2_from_dict = AbilityTooltipDetailsInfoSectionV2.from_dict(ability_tooltip_details_info_section_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


