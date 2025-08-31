# PlayerCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**ranked_badge_level** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**ranked_rank** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**ranked_subrank** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**slots** | [**List[PlayerCardSlot]**](PlayerCardSlot.md) |  | 

## Example

```python
from openapi_client.models.player_card import PlayerCard

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerCard from a JSON string
player_card_instance = PlayerCard.from_json(json)
# print the JSON string representation of the object
print(PlayerCard.to_json())

# convert the object into a dict
player_card_dict = player_card_instance.to_dict()
# create an instance of PlayerCard from a dict
player_card_from_dict = PlayerCard.from_dict(player_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


