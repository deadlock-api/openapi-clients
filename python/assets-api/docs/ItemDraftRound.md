# ItemDraftRound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chance_rare** | [**ItemTierV2**](ItemTierV2.md) |  | 
**chance_enhanced** | [**ItemTierV2**](ItemTierV2.md) |  | 

## Example

```python
from assets_deadlock_api_client.models.item_draft_round import ItemDraftRound

# TODO update the JSON string below
json = "{}"
# create an instance of ItemDraftRound from a JSON string
item_draft_round_instance = ItemDraftRound.from_json(json)
# print the JSON string representation of the object
print(ItemDraftRound.to_json())

# convert the object into a dict
item_draft_round_dict = item_draft_round_instance.to_dict()
# create an instance of ItemDraftRound from a dict
item_draft_round_from_dict = ItemDraftRound.from_dict(item_draft_round_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


