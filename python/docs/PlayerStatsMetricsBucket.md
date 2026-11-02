# PlayerStatsMetricsBucket

One bucket's metrics: `bucket`, and per metric the same values as an unbucketed response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **int** | The bucket&#39;s value: the hero id for &#x60;bucket&#x3D;hero&#x60;. | 

## Example

```python
from deadlock_api_client.models.player_stats_metrics_bucket import PlayerStatsMetricsBucket

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerStatsMetricsBucket from a JSON string
player_stats_metrics_bucket_instance = PlayerStatsMetricsBucket.from_json(json)
# print the JSON string representation of the object
print(PlayerStatsMetricsBucket.to_json())

# convert the object into a dict
player_stats_metrics_bucket_dict = player_stats_metrics_bucket_instance.to_dict()
# create an instance of PlayerStatsMetricsBucket from a dict
player_stats_metrics_bucket_from_dict = PlayerStatsMetricsBucket.from_dict(player_stats_metrics_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


