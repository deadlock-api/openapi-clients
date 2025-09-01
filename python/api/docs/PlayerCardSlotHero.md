# PlayerCardSlotHero


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 
**kills** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 

## Example

```python
from deadlock-api-client.models.player_card_slot_hero import PlayerCardSlotHero

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerCardSlotHero from a JSON string
player_card_slot_hero_instance = PlayerCardSlotHero.from_json(json)
# print the JSON string representation of the object
print(PlayerCardSlotHero.to_json())

# convert the object into a dict
player_card_slot_hero_dict = player_card_slot_hero_instance.to_dict()
# create an instance of PlayerCardSlotHero from a dict
player_card_slot_hero_from_dict = PlayerCardSlotHero.from_dict(player_card_slot_hero_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


