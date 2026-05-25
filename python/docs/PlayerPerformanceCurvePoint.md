# PlayerPerformanceCurvePoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists_avg** | **float** | Average assists at this time point | 
**assists_std** | **float** | Standard deviation of assists at this time point | 
**deaths_avg** | **float** | Average deaths at this time point | 
**deaths_std** | **float** | Standard deviation of deaths at this time point | 
**game_time** | **int** | The time point of the data. If &#x60;resolution&#x60; (default 10) is &gt; 0, this is a percentage (0, 10, ..., 100). If &#x60;resolution&#x60; is 0, this is the match time in seconds. | 
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


