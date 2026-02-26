# RawAbilityV2TooltipDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info_sections** | [**List[RawAbilityV2TooltipDetailsInfoSection]**](RawAbilityV2TooltipDetailsInfoSection.md) |  | [optional] 
**additional_header_properties** | **List[str]** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.raw_ability_v2_tooltip_details import RawAbilityV2TooltipDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RawAbilityV2TooltipDetails from a JSON string
raw_ability_v2_tooltip_details_instance = RawAbilityV2TooltipDetails.from_json(json)
# print the JSON string representation of the object
print(RawAbilityV2TooltipDetails.to_json())

# convert the object into a dict
raw_ability_v2_tooltip_details_dict = raw_ability_v2_tooltip_details_instance.to_dict()
# create an instance of RawAbilityV2TooltipDetails from a dict
raw_ability_v2_tooltip_details_from_dict = RawAbilityV2TooltipDetails.from_dict(raw_ability_v2_tooltip_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


