# ItemDraftsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | [**DraftBucket**](DraftBucket.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.item_drafts_value import ItemDraftsValue

# TODO update the JSON string below
json = "{}"
# create an instance of ItemDraftsValue from a JSON string
item_drafts_value_instance = ItemDraftsValue.from_json(json)
# print the JSON string representation of the object
print(ItemDraftsValue.to_json())

# convert the object into a dict
item_drafts_value_dict = item_drafts_value_instance.to_dict()
# create an instance of ItemDraftsValue from a dict
item_drafts_value_from_dict = ItemDraftsValue.from_dict(item_drafts_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


