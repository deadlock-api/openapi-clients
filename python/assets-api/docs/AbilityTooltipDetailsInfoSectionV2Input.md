# AbilityTooltipDetailsInfoSectionV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc_string** | **str** |  | [optional] 
**property_upgrade_required** | **str** |  | [optional] 
**properties_block** | [**List[AbilityTooltipDetailsInfoSectionPropertyBlockV2]**](AbilityTooltipDetailsInfoSectionPropertyBlockV2.md) |  | [optional] 
**basic_properties** | **List[str]** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.ability_tooltip_details_info_section_v2_input import AbilityTooltipDetailsInfoSectionV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of AbilityTooltipDetailsInfoSectionV2Input from a JSON string
ability_tooltip_details_info_section_v2_input_instance = AbilityTooltipDetailsInfoSectionV2Input.from_json(json)
# print the JSON string representation of the object
print(AbilityTooltipDetailsInfoSectionV2Input.to_json())

# convert the object into a dict
ability_tooltip_details_info_section_v2_input_dict = ability_tooltip_details_info_section_v2_input_instance.to_dict()
# create an instance of AbilityTooltipDetailsInfoSectionV2Input from a dict
ability_tooltip_details_info_section_v2_input_from_dict = AbilityTooltipDetailsInfoSectionV2Input.from_dict(ability_tooltip_details_info_section_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


