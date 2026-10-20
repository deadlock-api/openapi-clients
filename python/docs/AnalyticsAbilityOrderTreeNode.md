# AnalyticsAbilityOrderTreeNode

One node of the ability order tree: the players whose upgrade order starts with `abilities`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abilities** | **List[int]** | The order prefix: one entry per ability point spent, unlocks included. Its parent node is the prefix one entry shorter. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**avg_upgrade_time_s** | **float** | Average game time (in seconds) at which the last upgrade in &#x60;abilities&#x60; was bought. | 
**losses** | **int** |  | 
**matches** | **int** |  | 
**players** | **int** | Distinct players, counted exactly. | 
**total_assists** | **int** |  | 
**total_deaths** | **int** |  | 
**total_kills** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from deadlock_api_client.models.analytics_ability_order_tree_node import AnalyticsAbilityOrderTreeNode

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsAbilityOrderTreeNode from a JSON string
analytics_ability_order_tree_node_instance = AnalyticsAbilityOrderTreeNode.from_json(json)
# print the JSON string representation of the object
print(AnalyticsAbilityOrderTreeNode.to_json())

# convert the object into a dict
analytics_ability_order_tree_node_dict = analytics_ability_order_tree_node_instance.to_dict()
# create an instance of AnalyticsAbilityOrderTreeNode from a dict
analytics_ability_order_tree_node_from_dict = AnalyticsAbilityOrderTreeNode.from_dict(analytics_ability_order_tree_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


