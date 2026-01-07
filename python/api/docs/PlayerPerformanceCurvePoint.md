# PlayerPerformanceCurvePoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assists_avg** | **float** | Average assists at this timestamp | 
**assists_std** | **float** | Standard deviation of assists at this timestamp | 
**deaths_avg** | **float** | Average deaths at this timestamp | 
**deaths_std** | **float** | Standard deviation of deaths at this timestamp | 
**kills_avg** | **float** | Average kills at this timestamp | 
**kills_std** | **float** | Standard deviation of kills at this timestamp | 
**net_worth_avg** | **float** | Average net worth at this timestamp | 
**net_worth_std** | **float** | Standard deviation of net worth at this timestamp | 
**relative_timestamp** | **int** | Percentage interval of match duration (0%, 5%, 10%, ..., 100%) | 

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


