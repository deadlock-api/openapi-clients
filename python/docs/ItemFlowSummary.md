# ItemFlowSummary

Population-level totals for the (optionally locked) build path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_duration_s** | **float** | Average match duration (seconds) of the population. | 
**avg_net_worth** | **float** | Average final net worth of the population. | 
**losses** | **int** |  | 
**matches** | **int** |  | 
**players** | **int** |  | 
**total_assists** | **int** |  | 
**total_deaths** | **int** |  | 
**total_kills** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from deadlock_api_client.models.item_flow_summary import ItemFlowSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ItemFlowSummary from a JSON string
item_flow_summary_instance = ItemFlowSummary.from_json(json)
# print the JSON string representation of the object
print(ItemFlowSummary.to_json())

# convert the object into a dict
item_flow_summary_dict = item_flow_summary_instance.to_dict()
# create an instance of ItemFlowSummary from a dict
item_flow_summary_from_dict = ItemFlowSummary.from_dict(item_flow_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


