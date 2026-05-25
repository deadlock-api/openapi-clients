# NewPlayerMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abilities_upgraded** | **int** |  | 
**boss_damage** | **int** |  | 
**damage_taken** | **int** |  | 
**last_hits** | **int** |  | 
**mods_purchased** | **int** |  | 
**net_worth** | **int** |  | 
**orbs_denied** | **int** |  | 
**orbs_secured** | **int** |  | 
**player_damage** | **int** |  | 
**skill_tier_name** | **str** |  | 

## Example

```python
from deadlock_api_client.models.new_player_metrics import NewPlayerMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of NewPlayerMetrics from a JSON string
new_player_metrics_instance = NewPlayerMetrics.from_json(json)
# print the JSON string representation of the object
print(NewPlayerMetrics.to_json())

# convert the object into a dict
new_player_metrics_dict = new_player_metrics_instance.to_dict()
# create an instance of NewPlayerMetrics from a dict
new_player_metrics_from_dict = NewPlayerMetrics.from_dict(new_player_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


