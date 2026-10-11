# ItemFlowStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline** | [**models::ItemFlowSummary**](ItemFlowSummary.md) | Totals ignoring the locked build path (item filters only). Denominator for chained pick rate. | 
**edges** | [**Vec<models::ItemFlowEdge>**](ItemFlowEdge.md) |  | 
**leave_one_out** | [**Vec<models::ItemFlowLeaveOneOut>**](ItemFlowLeaveOneOut.md) | One entry per locked item, in request order: the totals of the locked build path without that item. `summary` against an entry is what that one item adds to the build. Empty without locks. | 
**nodes** | [**Vec<models::ItemFlowNode>**](ItemFlowNode.md) |  | 
**reached_per_column** | **Vec<u64>** | Distinct baseline games that bought any upgrade in each stage column (index = column). `reached / baseline.matches` shows how survivorship-selected a (late) stage is. | 
**reached_wins_per_column** | Option<**Vec<u64>**> | Of `reached_per_column`, the games that were won (index = column). `reached_wins / reached` is the win rate of games that got that far, the fair baseline for a build ending there. | [optional]
**summary** | [**models::ItemFlowSummary**](ItemFlowSummary.md) | Totals for the locked build-path population (all filters applied). Denominator for pick rate. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


