# BuildItemStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**builds** | **int** |  | 
**item_id** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/items&gt; | 

## Example

```python
from deadlock_api_client.models.build_item_stats import BuildItemStats

# TODO update the JSON string below
json = "{}"
# create an instance of BuildItemStats from a JSON string
build_item_stats_instance = BuildItemStats.from_json(json)
# print the JSON string representation of the object
print(BuildItemStats.to_json())

# convert the object into a dict
build_item_stats_dict = build_item_stats_instance.to_dict()
# create an instance of BuildItemStats from a dict
build_item_stats_from_dict = BuildItemStats.from_dict(build_item_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


