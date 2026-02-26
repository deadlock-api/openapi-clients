# RawAbilityV2TooltipDetailsInfoSectionPropertyBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc_string** | **str** |  | [optional] 
**properties** | [**List[RawAbilityV2TooltipDetailsInfoSectionPropertyBlockProperty]**](RawAbilityV2TooltipDetailsInfoSectionPropertyBlockProperty.md) |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.raw_ability_v2_tooltip_details_info_section_property_block import RawAbilityV2TooltipDetailsInfoSectionPropertyBlock

# TODO update the JSON string below
json = "{}"
# create an instance of RawAbilityV2TooltipDetailsInfoSectionPropertyBlock from a JSON string
raw_ability_v2_tooltip_details_info_section_property_block_instance = RawAbilityV2TooltipDetailsInfoSectionPropertyBlock.from_json(json)
# print the JSON string representation of the object
print(RawAbilityV2TooltipDetailsInfoSectionPropertyBlock.to_json())

# convert the object into a dict
raw_ability_v2_tooltip_details_info_section_property_block_dict = raw_ability_v2_tooltip_details_info_section_property_block_instance.to_dict()
# create an instance of RawAbilityV2TooltipDetailsInfoSectionPropertyBlock from a dict
raw_ability_v2_tooltip_details_info_section_property_block_from_dict = RawAbilityV2TooltipDetailsInfoSectionPropertyBlock.from_dict(raw_ability_v2_tooltip_details_info_section_property_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


