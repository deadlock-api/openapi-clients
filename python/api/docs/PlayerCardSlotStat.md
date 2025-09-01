# PlayerCardSlotStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stat_id** | **int** |  | [optional] 
**stat_score** | **int** |  | [optional] 

## Example

```python
from deadlock-api-client.models.player_card_slot_stat import PlayerCardSlotStat

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerCardSlotStat from a JSON string
player_card_slot_stat_instance = PlayerCardSlotStat.from_json(json)
# print the JSON string representation of the object
print(PlayerCardSlotStat.to_json())

# convert the object into a dict
player_card_slot_stat_dict = player_card_slot_stat_instance.to_dict()
# create an instance of PlayerCardSlotStat from a dict
player_card_slot_stat_from_dict = PlayerCardSlotStat.from_dict(player_card_slot_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


