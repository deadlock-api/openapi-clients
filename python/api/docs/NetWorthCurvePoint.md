# NetWorthCurvePoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | **float** | Average net worth at this timestamp | 
**percentile1** | **float** | 1st percentile net worth | 
**percentile10** | **float** | 10th percentile net worth | 
**percentile25** | **float** | 25th percentile net worth | 
**percentile5** | **float** | 5th percentile net worth | 
**percentile50** | **float** | 50th percentile net worth | 
**percentile75** | **float** | 75th percentile net worth | 
**percentile90** | **float** | 90th percentile net worth | 
**percentile95** | **float** | 95th percentile net worth | 
**percentile99** | **float** | 99th percentile net worth | 
**relative_timestamp** | **int** | Percentage interval of match duration (0%, 5%, 10%, ..., 100%) | 
**std** | **float** | Standard deviation of net worth at this timestamp | 

## Example

```python
from deadlock_api_client.models.net_worth_curve_point import NetWorthCurvePoint

# TODO update the JSON string below
json = "{}"
# create an instance of NetWorthCurvePoint from a JSON string
net_worth_curve_point_instance = NetWorthCurvePoint.from_json(json)
# print the JSON string representation of the object
print(NetWorthCurvePoint.to_json())

# convert the object into a dict
net_worth_curve_point_dict = net_worth_curve_point_instance.to_dict()
# create an instance of NetWorthCurvePoint from a dict
net_worth_curve_point_from_dict = NetWorthCurvePoint.from_dict(net_worth_curve_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


