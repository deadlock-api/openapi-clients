# AbilityTooltipDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_header_properties** | **List[str]** |  | [optional] 
**info_sections** | [**List[TooltipDetailsInfoSection]**](TooltipDetailsInfoSection.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.ability_tooltip_details import AbilityTooltipDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AbilityTooltipDetails from a JSON string
ability_tooltip_details_instance = AbilityTooltipDetails.from_json(json)
# print the JSON string representation of the object
print(AbilityTooltipDetails.to_json())

# convert the object into a dict
ability_tooltip_details_dict = ability_tooltip_details_instance.to_dict()
# create an instance of AbilityTooltipDetails from a dict
ability_tooltip_details_from_dict = AbilityTooltipDetails.from_dict(ability_tooltip_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


