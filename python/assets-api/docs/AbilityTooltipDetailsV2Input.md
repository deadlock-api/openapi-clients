# AbilityTooltipDetailsV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info_sections** | [**List[AbilityTooltipDetailsInfoSectionV2Input]**](AbilityTooltipDetailsInfoSectionV2Input.md) |  | [optional] 
**additional_header_properties** | **List[str]** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.ability_tooltip_details_v2_input import AbilityTooltipDetailsV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of AbilityTooltipDetailsV2Input from a JSON string
ability_tooltip_details_v2_input_instance = AbilityTooltipDetailsV2Input.from_json(json)
# print the JSON string representation of the object
print(AbilityTooltipDetailsV2Input.to_json())

# convert the object into a dict
ability_tooltip_details_v2_input_dict = ability_tooltip_details_v2_input_instance.to_dict()
# create an instance of AbilityTooltipDetailsV2Input from a dict
ability_tooltip_details_v2_input_from_dict = AbilityTooltipDetailsV2Input.from_dict(ability_tooltip_details_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


