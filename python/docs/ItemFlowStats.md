# ItemFlowStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline** | [**ItemFlowSummary**](ItemFlowSummary.md) | Totals ignoring the locked build path (item filters only). Denominator for chained pick rate. | 
**edges** | [**List[ItemFlowEdge]**](ItemFlowEdge.md) |  | 
**leave_one_out** | [**List[ItemFlowLeaveOneOut]**](ItemFlowLeaveOneOut.md) | One entry per locked item, in request order: the totals of the locked build path without that item. &#x60;summary&#x60; against an entry is what that one item adds to the build. Empty without locks. | 
**nodes** | [**List[ItemFlowNode]**](ItemFlowNode.md) |  | 
**reached_per_column** | **List[int]** | Distinct baseline games that bought any upgrade in each stage column (index &#x3D; column). &#x60;reached / baseline.matches&#x60; shows how survivorship-selected a (late) stage is. | 
**reached_wins_per_column** | **List[int]** | Of &#x60;reached_per_column&#x60;, the games that were won (index &#x3D; column). &#x60;reached_wins / reached&#x60; is the win rate of games that got that far, the fair baseline for a build ending there. | [optional] 
**summary** | [**ItemFlowSummary**](ItemFlowSummary.md) | Totals for the locked build-path population (all filters applied). Denominator for pick rate. | 
**summary_reached_per_column** | **List[int]** | &#x60;reached_per_column&#x60; for the locked build path&#39;s games (&#x60;summary&#x60;). Late stages hold long games only, so an item bought there is compared with the build&#39;s games that got that far. | [optional] 
**summary_reached_wins_per_column** | **List[int]** | Of &#x60;summary_reached_per_column&#x60;, the games that were won (index &#x3D; column). | [optional] 

## Example

```python
from deadlock_api_client.models.item_flow_stats import ItemFlowStats

# TODO update the JSON string below
json = "{}"
# create an instance of ItemFlowStats from a JSON string
item_flow_stats_instance = ItemFlowStats.from_json(json)
# print the JSON string representation of the object
print(ItemFlowStats.to_json())

# convert the object into a dict
item_flow_stats_dict = item_flow_stats_instance.to_dict()
# create an instance of ItemFlowStats from a dict
item_flow_stats_from_dict = ItemFlowStats.from_dict(item_flow_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


