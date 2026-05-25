# ItemPermutationStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ids** | **List[int]** | See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | 
**losses** | **int** |  | 
**matches** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from deadlock_api_client.models.item_permutation_stats import ItemPermutationStats

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPermutationStats from a JSON string
item_permutation_stats_instance = ItemPermutationStats.from_json(json)
# print the JSON string representation of the object
print(ItemPermutationStats.to_json())

# convert the object into a dict
item_permutation_stats_dict = item_permutation_stats_instance.to_dict()
# create an instance of ItemPermutationStats from a dict
item_permutation_stats_from_dict = ItemPermutationStats.from_dict(item_permutation_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


