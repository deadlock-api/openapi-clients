# DeadlockApiClient.Model.ItemFlowStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Baseline** | [**ItemFlowSummary**](ItemFlowSummary.md) | Totals ignoring the locked build path (item filters only). Denominator for chained pick rate. | 
**Edges** | [**List&lt;ItemFlowEdge&gt;**](ItemFlowEdge.md) |  | 
**Nodes** | [**List&lt;ItemFlowNode&gt;**](ItemFlowNode.md) |  | 
**ReachedPerColumn** | **List&lt;long&gt;** | Distinct baseline games that bought any upgrade in each stage column (index &#x3D; column). &#x60;reached / baseline.matches&#x60; shows how survivorship-selected a (late) stage is. | 
**Summary** | [**ItemFlowSummary**](ItemFlowSummary.md) | Totals for the locked build-path population (all filters applied). Denominator for pick rate. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

