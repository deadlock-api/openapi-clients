# ItemStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **int** |  | 
**item_id** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | 
**losses** | **int** |  | 
**matches** | **int** |  | 
**players** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from deadlock_api_client.models.item_stats import ItemStats

# TODO update the JSON string below
json = "{}"
# create an instance of ItemStats from a JSON string
item_stats_instance = ItemStats.from_json(json)
# print the JSON string representation of the object
print(ItemStats.to_json())

# convert the object into a dict
item_stats_dict = item_stats_instance.to_dict()
# create an instance of ItemStats from a dict
item_stats_from_dict = ItemStats.from_dict(item_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


