# ItemDraftRoundPerGameRound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chance_rare** | [**OutcomeToWeights**](OutcomeToWeights.md) |  | 
**chance_enhanced** | [**OutcomeToWeights**](OutcomeToWeights.md) |  | 
**item_draft_rounds** | [**List[ItemDraftRound]**](ItemDraftRound.md) |  | 

## Example

```python
from assets_deadlock_api_client.models.item_draft_round_per_game_round import ItemDraftRoundPerGameRound

# TODO update the JSON string below
json = "{}"
# create an instance of ItemDraftRoundPerGameRound from a JSON string
item_draft_round_per_game_round_instance = ItemDraftRoundPerGameRound.from_json(json)
# print the JSON string representation of the object
print(ItemDraftRoundPerGameRound.to_json())

# convert the object into a dict
item_draft_round_per_game_round_dict = item_draft_round_per_game_round_instance.to_dict()
# create an instance of ItemDraftRoundPerGameRound from a dict
item_draft_round_per_game_round_from_dict = ItemDraftRoundPerGameRound.from_dict(item_draft_round_per_game_round_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


