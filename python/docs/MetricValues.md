# MetricValues

One metric's distribution over single matches. Every value is `null` (NaN) when no matching match has the metric, e.g. `first_permanent_buff_time_s` for matches before build 6712.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | **float** |  | 
**percentile1** | **float** |  | 
**percentile10** | **float** |  | 
**percentile25** | **float** |  | 
**percentile5** | **float** |  | 
**percentile50** | **float** |  | 
**percentile75** | **float** |  | 
**percentile90** | **float** |  | 
**percentile95** | **float** |  | 
**percentile99** | **float** |  | 
**std** | **float** |  | 

## Example

```python
from deadlock_api_client.models.metric_values import MetricValues

# TODO update the JSON string below
json = "{}"
# create an instance of MetricValues from a JSON string
metric_values_instance = MetricValues.from_json(json)
# print the JSON string representation of the object
print(MetricValues.to_json())

# convert the object into a dict
metric_values_dict = metric_values_instance.to_dict()
# create an instance of MetricValues from a dict
metric_values_from_dict = MetricValues.from_dict(metric_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


