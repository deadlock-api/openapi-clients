# ItemTooltipBacker

Item tooltip background of one slot type: the backer, its alpha mask and the color layer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backer** | [**ImagePair**](ImagePair.md) |  | 
**color** | [**ImagePair**](ImagePair.md) |  | 
**mask** | [**ImagePair**](ImagePair.md) |  | 

## Example

```python
from deadlock_api_client.models.item_tooltip_backer import ItemTooltipBacker

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTooltipBacker from a JSON string
item_tooltip_backer_instance = ItemTooltipBacker.from_json(json)
# print the JSON string representation of the object
print(ItemTooltipBacker.to_json())

# convert the object into a dict
item_tooltip_backer_dict = item_tooltip_backer_instance.to_dict()
# create an instance of ItemTooltipBacker from a dict
item_tooltip_backer_from_dict = ItemTooltipBacker.from_dict(item_tooltip_backer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


