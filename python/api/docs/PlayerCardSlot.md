# PlayerCardSlot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hero** | [**PlayerCardSlotHero**](PlayerCardSlotHero.md) |  | [optional] 
**slot_id** | **int** |  | [optional] 
**stat** | [**PlayerCardSlotStat**](PlayerCardSlotStat.md) |  | [optional] 

## Example

```python
from openapi_client.models.player_card_slot import PlayerCardSlot

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerCardSlot from a JSON string
player_card_slot_instance = PlayerCardSlot.from_json(json)
# print the JSON string representation of the object
print(PlayerCardSlot.to_json())

# convert the object into a dict
player_card_slot_dict = player_card_slot_instance.to_dict()
# create an instance of PlayerCardSlot from a dict
player_card_slot_from_dict = PlayerCardSlot.from_dict(player_card_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


