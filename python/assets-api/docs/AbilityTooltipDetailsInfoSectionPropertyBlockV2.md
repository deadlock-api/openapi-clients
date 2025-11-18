# AbilityTooltipDetailsInfoSectionPropertyBlockV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc_string** | **str** |  | [optional] 
**properties** | [**List[AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty]**](AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty.md) |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.ability_tooltip_details_info_section_property_block_v2 import AbilityTooltipDetailsInfoSectionPropertyBlockV2

# TODO update the JSON string below
json = "{}"
# create an instance of AbilityTooltipDetailsInfoSectionPropertyBlockV2 from a JSON string
ability_tooltip_details_info_section_property_block_v2_instance = AbilityTooltipDetailsInfoSectionPropertyBlockV2.from_json(json)
# print the JSON string representation of the object
print(AbilityTooltipDetailsInfoSectionPropertyBlockV2.to_json())

# convert the object into a dict
ability_tooltip_details_info_section_property_block_v2_dict = ability_tooltip_details_info_section_property_block_v2_instance.to_dict()
# create an instance of AbilityTooltipDetailsInfoSectionPropertyBlockV2 from a dict
ability_tooltip_details_info_section_property_block_v2_from_dict = AbilityTooltipDetailsInfoSectionPropertyBlockV2.from_dict(ability_tooltip_details_info_section_property_block_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


