# TooltipDetailsBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc_string** | **str** |  | [optional] 
**properties** | [**List[TooltipDetailsBlockProperty]**](TooltipDetailsBlockProperty.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.tooltip_details_block import TooltipDetailsBlock

# TODO update the JSON string below
json = "{}"
# create an instance of TooltipDetailsBlock from a JSON string
tooltip_details_block_instance = TooltipDetailsBlock.from_json(json)
# print the JSON string representation of the object
print(TooltipDetailsBlock.to_json())

# convert the object into a dict
tooltip_details_block_dict = tooltip_details_block_instance.to_dict()
# create an instance of TooltipDetailsBlock from a dict
tooltip_details_block_from_dict = TooltipDetailsBlock.from_dict(tooltip_details_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


