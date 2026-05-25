# TooltipDetailsBlockProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**important_property** | **str** |  | [optional] 
**important_property_icon** | **str** |  | [optional] 
**requires_ability_upgrade** | **bool** |  | [optional] 
**show_property_value** | **bool** |  | [optional] 
**status_effect_name** | **str** |  | [optional] 
**status_effect_value** | **str** |  | [optional] 

## Example

```python
from deadlock_api_client.models.tooltip_details_block_property import TooltipDetailsBlockProperty

# TODO update the JSON string below
json = "{}"
# create an instance of TooltipDetailsBlockProperty from a JSON string
tooltip_details_block_property_instance = TooltipDetailsBlockProperty.from_json(json)
# print the JSON string representation of the object
print(TooltipDetailsBlockProperty.to_json())

# convert the object into a dict
tooltip_details_block_property_dict = tooltip_details_block_property_instance.to_dict()
# create an instance of TooltipDetailsBlockProperty from a dict
tooltip_details_block_property_from_dict = TooltipDetailsBlockProperty.from_dict(tooltip_details_block_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


