# PlayerPerformanceCurvePoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists_avg** | **float** | Average assists at this time point | 
**assists_std** | **float** | Standard deviation of assists at this time point | 
**deaths_avg** | **float** | Average deaths at this time point | 
**deaths_std** | **float** | Standard deviation of deaths at this time point | 
**game_time** | **int** | The time point of the data. If &#x60;resolution&#x60; (default 10) is &gt; 0, this is a percentage (0, 10, ..., 100). If &#x60;resolution&#x60; is 0, this is the match time in seconds. | 
**gold_boss_avg** | **float** | Average souls earned from objectives at this time point | 
**gold_boss_orb_avg** | **float** | Average souls earned from secured objective orbs at this time point | 
**gold_death_loss_avg** | **float** | Average souls lost on death at this time point | 
**gold_denied_avg** | **float** | Average souls denied to enemies at this time point | 
**gold_lane_creep_avg** | **float** | Average souls earned from lane creeps at this time point | 
**gold_lane_creep_orbs_avg** | **float** | Average souls earned from secured lane-creep orbs at this time point | 
**gold_neutral_creep_avg** | **float** | Average souls earned from neutral (jungle) creeps at this time point | 
**gold_neutral_creep_orbs_avg** | **float** | Average souls earned from secured neutral-creep orbs at this time point | 
**gold_player_avg** | **float** | Average souls earned from hero kills at this time point | 
**gold_player_orbs_avg** | **float** | Average souls earned from secured hero-kill orbs at this time point | 
**gold_treasure_avg** | **float** | Average souls earned from the urn at this time point | 
**kills_avg** | **float** | Average kills at this time point | 
**kills_std** | **float** | Standard deviation of kills at this time point | 
**net_worth_avg** | **float** | Average net worth at this time point | 
**net_worth_std** | **float** | Standard deviation of net worth at this time point | 

## Example

```python
from deadlock_api_client.models.player_performance_curve_point import PlayerPerformanceCurvePoint

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerPerformanceCurvePoint from a JSON string
player_performance_curve_point_instance = PlayerPerformanceCurvePoint.from_json(json)
# print the JSON string representation of the object
print(PlayerPerformanceCurvePoint.to_json())

# convert the object into a dict
player_performance_curve_point_dict = player_performance_curve_point_instance.to_dict()
# create an instance of PlayerPerformanceCurvePoint from a dict
player_performance_curve_point_from_dict = PlayerPerformanceCurvePoint.from_dict(player_performance_curve_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


