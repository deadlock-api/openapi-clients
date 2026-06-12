# ItemFlowNode

A single item, aggregated within one column of the flow graph.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_win_rate** | **float** | Win rate standardized to the stage&#39;s net-worth-at-buy distribution, removing the \&quot;richer buyers win more\&quot; confound. See the endpoint description. | 
**avg_net_worth_at_buy** | **float** | Average net worth of buyers at the moment they bought this item (confound visibility). | 
**column** | **int** | The phase column (0-based) the item was bought in. | 
**item_id** | **int** | See more: &lt;https://api.deadlock-api.com/v1/assets/items&gt; | 
**losses** | **int** |  | 
**matches** | **int** |  | 
**players** | **int** |  | 
**total_assists** | **int** |  | 
**total_deaths** | **int** |  | 
**total_kills** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from deadlock_api_client.models.item_flow_node import ItemFlowNode

# TODO update the JSON string below
json = "{}"
# create an instance of ItemFlowNode from a JSON string
item_flow_node_instance = ItemFlowNode.from_json(json)
# print the JSON string representation of the object
print(ItemFlowNode.to_json())

# convert the object into a dict
item_flow_node_dict = item_flow_node_instance.to_dict()
# create an instance of ItemFlowNode from a dict
item_flow_node_from_dict = ItemFlowNode.from_dict(item_flow_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


