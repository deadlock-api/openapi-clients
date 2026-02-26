# RawAbilityV2TooltipDetailsInfoSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_upgrade_required** | **str** |  | [optional] 
**loc_string** | **str** |  | [optional] 
**properties_block** | [**List[RawAbilityV2TooltipDetailsInfoSectionPropertyBlock]**](RawAbilityV2TooltipDetailsInfoSectionPropertyBlock.md) |  | [optional] 
**basic_properties** | **List[str]** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.raw_ability_v2_tooltip_details_info_section import RawAbilityV2TooltipDetailsInfoSection

# TODO update the JSON string below
json = "{}"
# create an instance of RawAbilityV2TooltipDetailsInfoSection from a JSON string
raw_ability_v2_tooltip_details_info_section_instance = RawAbilityV2TooltipDetailsInfoSection.from_json(json)
# print the JSON string representation of the object
print(RawAbilityV2TooltipDetailsInfoSection.to_json())

# convert the object into a dict
raw_ability_v2_tooltip_details_info_section_dict = raw_ability_v2_tooltip_details_info_section_instance.to_dict()
# create an instance of RawAbilityV2TooltipDetailsInfoSection from a dict
raw_ability_v2_tooltip_details_info_section_from_dict = RawAbilityV2TooltipDetailsInfoSection.from_dict(raw_ability_v2_tooltip_details_info_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


