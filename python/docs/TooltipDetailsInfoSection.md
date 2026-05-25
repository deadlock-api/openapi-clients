# TooltipDetailsInfoSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_properties** | **List[str]** |  | [optional] 
**loc_string** | **str** |  | [optional] 
**properties_block** | [**List[TooltipDetailsBlock]**](TooltipDetailsBlock.md) |  | [optional] 
**property_upgrade_required** | **str** |  | [optional] 

## Example

```python
from deadlock_api_client.models.tooltip_details_info_section import TooltipDetailsInfoSection

# TODO update the JSON string below
json = "{}"
# create an instance of TooltipDetailsInfoSection from a JSON string
tooltip_details_info_section_instance = TooltipDetailsInfoSection.from_json(json)
# print the JSON string representation of the object
print(TooltipDetailsInfoSection.to_json())

# convert the object into a dict
tooltip_details_info_section_dict = tooltip_details_info_section_instance.to_dict()
# create an instance of TooltipDetailsInfoSection from a dict
tooltip_details_info_section_from_dict = TooltipDetailsInfoSection.from_dict(tooltip_details_info_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


