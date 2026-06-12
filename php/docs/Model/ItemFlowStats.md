# ItemFlowStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline** | [**\OpenAPI\Client\Model\ItemFlowSummary**](ItemFlowSummary.md) | Totals ignoring the locked build path (item filters only). Denominator for chained pick rate. |
**edges** | [**\OpenAPI\Client\Model\ItemFlowEdge[]**](ItemFlowEdge.md) |  |
**nodes** | [**\OpenAPI\Client\Model\ItemFlowNode[]**](ItemFlowNode.md) |  |
**reached_per_column** | **int[]** | Distinct baseline games that bought any upgrade in each stage column (index &#x3D; column). &#x60;reached / baseline.matches&#x60; shows how survivorship-selected a (late) stage is. |
**summary** | [**\OpenAPI\Client\Model\ItemFlowSummary**](ItemFlowSummary.md) | Totals for the locked build-path population (all filters applied). Denominator for pick rate. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
