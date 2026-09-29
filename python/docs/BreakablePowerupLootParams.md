# BreakablePowerupLootParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loot_list_deck_size** | **int** |  | [optional] 
**pickups_by_match_time_mins** | **Dict[str, Dict[str, float]]** | Match time in minutes (string key) from which a loot table applies, mapped to &#x60;{pickup_name: relative weight}&#x60;. | 

## Example

```python
from deadlock_api_client.models.breakable_powerup_loot_params import BreakablePowerupLootParams

# TODO update the JSON string below
json = "{}"
# create an instance of BreakablePowerupLootParams from a JSON string
breakable_powerup_loot_params_instance = BreakablePowerupLootParams.from_json(json)
# print the JSON string representation of the object
print(BreakablePowerupLootParams.to_json())

# convert the object into a dict
breakable_powerup_loot_params_dict = breakable_powerup_loot_params_instance.to_dict()
# create an instance of BreakablePowerupLootParams from a dict
breakable_powerup_loot_params_from_dict = BreakablePowerupLootParams.from_dict(breakable_powerup_loot_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


