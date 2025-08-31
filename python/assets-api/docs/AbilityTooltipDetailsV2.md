# AbilityTooltipDetailsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info_sections** | [**List[AbilityTooltipDetailsInfoSectionV2]**](AbilityTooltipDetailsInfoSectionV2.md) |  | [optional] 
**additional_header_properties** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.ability_tooltip_details_v2 import AbilityTooltipDetailsV2

# TODO update the JSON string below
json = "{}"
# create an instance of AbilityTooltipDetailsV2 from a JSON string
ability_tooltip_details_v2_instance = AbilityTooltipDetailsV2.from_json(json)
# print the JSON string representation of the object
print(AbilityTooltipDetailsV2.to_json())

# convert the object into a dict
ability_tooltip_details_v2_dict = ability_tooltip_details_v2_instance.to_dict()
# create an instance of AbilityTooltipDetailsV2 from a dict
ability_tooltip_details_v2_from_dict = AbilityTooltipDetailsV2.from_dict(ability_tooltip_details_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


