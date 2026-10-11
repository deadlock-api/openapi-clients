# ItemFlowStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline** | [**\OpenAPI\Client\Model\ItemFlowSummary**](ItemFlowSummary.md) | Totals ignoring the locked build path (item filters only). Denominator for chained pick rate. |
**edges** | [**\OpenAPI\Client\Model\ItemFlowEdge[]**](ItemFlowEdge.md) |  |
**leave_one_out** | [**\OpenAPI\Client\Model\ItemFlowLeaveOneOut[]**](ItemFlowLeaveOneOut.md) | One entry per locked item, in request order: the totals of the locked build path without that item. &#x60;summary&#x60; against an entry is what that one item adds to the build. Empty without locks. |
**nodes** | [**\OpenAPI\Client\Model\ItemFlowNode[]**](ItemFlowNode.md) |  |
**reached_per_column** | **int[]** | Distinct baseline games that bought any upgrade in each stage column (index &#x3D; column). &#x60;reached / baseline.matches&#x60; shows how survivorship-selected a (late) stage is. |
**reached_wins_per_column** | **int[]** | Of &#x60;reached_per_column&#x60;, the games that were won (index &#x3D; column). &#x60;reached_wins / reached&#x60; is the win rate of games that got that far, the fair baseline for a build ending there. | [optional]
**summary** | [**\OpenAPI\Client\Model\ItemFlowSummary**](ItemFlowSummary.md) | Totals for the locked build-path population (all filters applied). Denominator for pick rate. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
