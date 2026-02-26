# RawAbilityV2TooltipDetailsInfoSectionPropertyBlockProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requires_ability_upgrade** | **bool** |  | [optional] 
**show_property_value** | **bool** |  | [optional] 
**important_property** | **str** |  | [optional] 
**status_effect_value** | **str** |  | [optional] 
**important_property_icon_path** | **str** |  | [readonly] 

## Example

```python
from assets_deadlock_api_client.models.raw_ability_v2_tooltip_details_info_section_property_block_property import RawAbilityV2TooltipDetailsInfoSectionPropertyBlockProperty

# TODO update the JSON string below
json = "{}"
# create an instance of RawAbilityV2TooltipDetailsInfoSectionPropertyBlockProperty from a JSON string
raw_ability_v2_tooltip_details_info_section_property_block_property_instance = RawAbilityV2TooltipDetailsInfoSectionPropertyBlockProperty.from_json(json)
# print the JSON string representation of the object
print(RawAbilityV2TooltipDetailsInfoSectionPropertyBlockProperty.to_json())

# convert the object into a dict
raw_ability_v2_tooltip_details_info_section_property_block_property_dict = raw_ability_v2_tooltip_details_info_section_property_block_property_instance.to_dict()
# create an instance of RawAbilityV2TooltipDetailsInfoSectionPropertyBlockProperty from a dict
raw_ability_v2_tooltip_details_info_section_property_block_property_from_dict = RawAbilityV2TooltipDetailsInfoSectionPropertyBlockProperty.from_dict(raw_ability_v2_tooltip_details_info_section_property_block_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


