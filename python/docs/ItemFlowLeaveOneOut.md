# ItemFlowLeaveOneOut

The locked build path without one of its locked items: how the population changes when that item's constraint is dropped and every other one kept.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **int** | Its locked stage column. | 
**item_id** | **int** | The locked item left out. See more: &lt;https://api.deadlock-api.com/v1/assets/items&gt; | 
**matches** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from deadlock_api_client.models.item_flow_leave_one_out import ItemFlowLeaveOneOut

# TODO update the JSON string below
json = "{}"
# create an instance of ItemFlowLeaveOneOut from a JSON string
item_flow_leave_one_out_instance = ItemFlowLeaveOneOut.from_json(json)
# print the JSON string representation of the object
print(ItemFlowLeaveOneOut.to_json())

# convert the object into a dict
item_flow_leave_one_out_dict = item_flow_leave_one_out_instance.to_dict()
# create an instance of ItemFlowLeaveOneOut from a dict
item_flow_leave_one_out_from_dict = ItemFlowLeaveOneOut.from_dict(item_flow_leave_one_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


