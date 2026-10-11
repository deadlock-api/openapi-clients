# DeadlockApiClient.Model.ItemFlowStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Baseline** | [**ItemFlowSummary**](ItemFlowSummary.md) | Totals ignoring the locked build path (item filters only). Denominator for chained pick rate. | 
**Edges** | [**List&lt;ItemFlowEdge&gt;**](ItemFlowEdge.md) |  | 
**LeaveOneOut** | [**List&lt;ItemFlowLeaveOneOut&gt;**](ItemFlowLeaveOneOut.md) | One entry per locked item, in request order: the totals of the locked build path without that item. &#x60;summary&#x60; against an entry is what that one item adds to the build. Empty without locks. | 
**Nodes** | [**List&lt;ItemFlowNode&gt;**](ItemFlowNode.md) |  | 
**ReachedPerColumn** | **List&lt;long&gt;** | Distinct baseline games that bought any upgrade in each stage column (index &#x3D; column). &#x60;reached / baseline.matches&#x60; shows how survivorship-selected a (late) stage is. | 
**Summary** | [**ItemFlowSummary**](ItemFlowSummary.md) | Totals for the locked build-path population (all filters applied). Denominator for pick rate. | 
**ReachedWinsPerColumn** | **List&lt;long&gt;** | Of &#x60;reached_per_column&#x60;, the games that were won (index &#x3D; column). &#x60;reached_wins / reached&#x60; is the win rate of games that got that far, the fair baseline for a build ending there. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

