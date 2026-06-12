# ItemFlowStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline** | [**ItemFlowSummary**](ItemFlowSummary.md) | Totals ignoring the locked build path (item filters only). Denominator for chained pick rate. | [default to undefined]
**edges** | [**Array&lt;ItemFlowEdge&gt;**](ItemFlowEdge.md) |  | [default to undefined]
**nodes** | [**Array&lt;ItemFlowNode&gt;**](ItemFlowNode.md) |  | [default to undefined]
**reached_per_column** | **Array&lt;number&gt;** | Distinct baseline games that bought any upgrade in each stage column (index &#x3D; column). &#x60;reached / baseline.matches&#x60; shows how survivorship-selected a (late) stage is. | [default to undefined]
**summary** | [**ItemFlowSummary**](ItemFlowSummary.md) | Totals for the locked build-path population (all filters applied). Denominator for pick rate. | [default to undefined]

## Example

```typescript
import { ItemFlowStats } from 'deadlock_api_client';

const instance: ItemFlowStats = {
    baseline,
    edges,
    nodes,
    reached_per_column,
    summary,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
