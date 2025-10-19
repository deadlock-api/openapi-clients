# AbilityTooltipDetailsV2Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info_sections** | [**List[AbilityTooltipDetailsInfoSectionV2Output]**](AbilityTooltipDetailsInfoSectionV2Output.md) |  | [optional] 
**additional_header_properties** | **List[str]** |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.ability_tooltip_details_v2_output import AbilityTooltipDetailsV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of AbilityTooltipDetailsV2Output from a JSON string
ability_tooltip_details_v2_output_instance = AbilityTooltipDetailsV2Output.from_json(json)
# print the JSON string representation of the object
print(AbilityTooltipDetailsV2Output.to_json())

# convert the object into a dict
ability_tooltip_details_v2_output_dict = ability_tooltip_details_v2_output_instance.to_dict()
# create an instance of AbilityTooltipDetailsV2Output from a dict
ability_tooltip_details_v2_output_from_dict = AbilityTooltipDetailsV2Output.from_dict(ability_tooltip_details_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


