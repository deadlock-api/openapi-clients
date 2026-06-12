# ItemFlowStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline** | [**models::ItemFlowSummary**](ItemFlowSummary.md) | Totals ignoring the locked build path (item filters only). Denominator for chained pick rate. | 
**edges** | [**Vec<models::ItemFlowEdge>**](ItemFlowEdge.md) |  | 
**nodes** | [**Vec<models::ItemFlowNode>**](ItemFlowNode.md) |  | 
**reached_per_column** | **Vec<u64>** | Distinct baseline games that bought any upgrade in each stage column (index = column). `reached / baseline.matches` shows how survivorship-selected a (late) stage is. | 
**summary** | [**models::ItemFlowSummary**](ItemFlowSummary.md) | Totals for the locked build-path population (all filters applied). Denominator for pick rate. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


