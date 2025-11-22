# ItemGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shop_group** | **str** |  | 
**upgrades** | **List[str]** |  | 

## Example

```python
from assets_deadlock_api_client.models.item_group import ItemGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ItemGroup from a JSON string
item_group_instance = ItemGroup.from_json(json)
# print the JSON string representation of the object
print(ItemGroup.to_json())

# convert the object into a dict
item_group_dict = item_group_instance.to_dict()
# create an instance of ItemGroup from a dict
item_group_from_dict = ItemGroup.from_dict(item_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


