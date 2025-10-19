# AbilityTooltipDetailsInfoSectionV2Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc_string** | **str** |  | [optional] 
**property_upgrade_required** | **str** |  | [optional] 
**properties_block** | [**List[AbilityTooltipDetailsInfoSectionPropertyBlockV2]**](AbilityTooltipDetailsInfoSectionPropertyBlockV2.md) |  | [optional] 
**basic_properties** | **List[str]** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.ability_tooltip_details_info_section_v2_output import AbilityTooltipDetailsInfoSectionV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of AbilityTooltipDetailsInfoSectionV2Output from a JSON string
ability_tooltip_details_info_section_v2_output_instance = AbilityTooltipDetailsInfoSectionV2Output.from_json(json)
# print the JSON string representation of the object
print(AbilityTooltipDetailsInfoSectionV2Output.to_json())

# convert the object into a dict
ability_tooltip_details_info_section_v2_output_dict = ability_tooltip_details_info_section_v2_output_instance.to_dict()
# create an instance of AbilityTooltipDetailsInfoSectionV2Output from a dict
ability_tooltip_details_info_section_v2_output_from_dict = AbilityTooltipDetailsInfoSectionV2Output.from_dict(ability_tooltip_details_info_section_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


