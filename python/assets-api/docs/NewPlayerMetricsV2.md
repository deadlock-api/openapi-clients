# NewPlayerMetricsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill_tier_name** | **str** |  | 
**net_worth** | **int** |  | 
**damage_taken** | **int** |  | 
**boss_damage** | **int** |  | 
**player_damage** | **int** |  | 
**last_hits** | **int** |  | 
**orbs_secured** | **int** |  | 
**orbs_denied** | **int** |  | 
**abilities_upgraded** | **int** |  | 
**mods_purchased** | **int** |  | 

## Example

```python
from assets_deadlock_api_client.models.new_player_metrics_v2 import NewPlayerMetricsV2

# TODO update the JSON string below
json = "{}"
# create an instance of NewPlayerMetricsV2 from a JSON string
new_player_metrics_v2_instance = NewPlayerMetricsV2.from_json(json)
# print the JSON string representation of the object
print(NewPlayerMetricsV2.to_json())

# convert the object into a dict
new_player_metrics_v2_dict = new_player_metrics_v2_instance.to_dict()
# create an instance of NewPlayerMetricsV2 from a dict
new_player_metrics_v2_from_dict = NewPlayerMetricsV2.from_dict(new_player_metrics_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


