# ItemFlowEdge

A transition between an item in one column and an item in the next column, counted across players who purchased both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_column** | **int** | The column of the source item. | 
**from_item_id** | **int** |  | 
**losses** | **int** |  | 
**matches** | **int** |  | 
**to_item_id** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from deadlock_api_client.models.item_flow_edge import ItemFlowEdge

# TODO update the JSON string below
json = "{}"
# create an instance of ItemFlowEdge from a JSON string
item_flow_edge_instance = ItemFlowEdge.from_json(json)
# print the JSON string representation of the object
print(ItemFlowEdge.to_json())

# convert the object into a dict
item_flow_edge_dict = item_flow_edge_instance.to_dict()
# create an instance of ItemFlowEdge from a dict
item_flow_edge_from_dict = ItemFlowEdge.from_dict(item_flow_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


