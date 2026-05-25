# MetricIngestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Steam account id (&#x60;UInt32&#x60;) of the player this metric is about | 
**game_mode** | **str** | Game mode this metric applies to (e.g. \&quot;speedrun\&quot;) | 
**game_mode_version** | **str** | Optional game-mode version tag (e.g. \&quot;v2\&quot;, \&quot;season3\&quot;) for versioning leaderboards | [optional] 
**map** | **str** | Optional map identifier the metric was produced on | [optional] 
**metadata** | **Dict[str, str]** | Free-form key/value metadata for game-mode-specific context | [optional] 
**metric_name** | **str** | Name of the metric (e.g. &#x60;run_time&#x60;) | 
**metric_value** | **float** | The primary numeric measurement for this metric | 
**region** | **str** | Region the server is located in (e.g. \&quot;eu\&quot;, \&quot;na\&quot;) | 
**server_id** | **str** | Unique identifier for the game server reporting the metric | 

## Example

```python
from deadlock_api_client.models.metric_ingest_request import MetricIngestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetricIngestRequest from a JSON string
metric_ingest_request_instance = MetricIngestRequest.from_json(json)
# print the JSON string representation of the object
print(MetricIngestRequest.to_json())

# convert the object into a dict
metric_ingest_request_dict = metric_ingest_request_instance.to_dict()
# create an instance of MetricIngestRequest from a dict
metric_ingest_request_from_dict = MetricIngestRequest.from_dict(metric_ingest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


