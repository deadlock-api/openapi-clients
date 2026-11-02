# PlayerStatsMetricsResponse

One metrics object without `bucket`, one per bucket with it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from deadlock_api_client.models.player_stats_metrics_response import PlayerStatsMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerStatsMetricsResponse from a JSON string
player_stats_metrics_response_instance = PlayerStatsMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(PlayerStatsMetricsResponse.to_json())

# convert the object into a dict
player_stats_metrics_response_dict = player_stats_metrics_response_instance.to_dict()
# create an instance of PlayerStatsMetricsResponse from a dict
player_stats_metrics_response_from_dict = PlayerStatsMetricsResponse.from_dict(player_stats_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


