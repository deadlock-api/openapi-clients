# ItemTooltipBackers

Item tooltip backgrounds, one per item slot type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spirit** | [**ItemTooltipBacker**](ItemTooltipBacker.md) |  | 
**vitality** | [**ItemTooltipBacker**](ItemTooltipBacker.md) |  | 
**weapon** | [**ItemTooltipBacker**](ItemTooltipBacker.md) |  | 

## Example

```python
from deadlock_api_client.models.item_tooltip_backers import ItemTooltipBackers

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTooltipBackers from a JSON string
item_tooltip_backers_instance = ItemTooltipBackers.from_json(json)
# print the JSON string representation of the object
print(ItemTooltipBackers.to_json())

# convert the object into a dict
item_tooltip_backers_dict = item_tooltip_backers_instance.to_dict()
# create an instance of ItemTooltipBackers from a dict
item_tooltip_backers_from_dict = ItemTooltipBackers.from_dict(item_tooltip_backers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


