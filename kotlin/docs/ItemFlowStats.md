
# ItemFlowStats

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **baseline** | [**ItemFlowSummary**](ItemFlowSummary.md) | Totals ignoring the locked build path (item filters only). Denominator for chained pick rate. |  |
| **edges** | [**kotlin.collections.List&lt;ItemFlowEdge&gt;**](ItemFlowEdge.md) |  |  |
| **nodes** | [**kotlin.collections.List&lt;ItemFlowNode&gt;**](ItemFlowNode.md) |  |  |
| **reachedPerColumn** | **kotlin.collections.List&lt;kotlin.Long&gt;** | Distinct baseline games that bought any upgrade in each stage column (index &#x3D; column). &#x60;reached / baseline.matches&#x60; shows how survivorship-selected a (late) stage is. |  |
| **summary** | [**ItemFlowSummary**](ItemFlowSummary.md) | Totals for the locked build-path population (all filters applied). Denominator for pick rate. |  |



