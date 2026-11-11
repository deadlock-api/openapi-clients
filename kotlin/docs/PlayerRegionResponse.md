
# PlayerRegionResponse

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Int** |  |  |
| **history** | [**kotlin.collections.List&lt;PlayerClusterMonth&gt;**](PlayerClusterMonth.md) | Matches per month and server cluster, newest month first. |  |
| **region** | **kotlin.String** | The region the player played most matches in during their latest month with a known region. &#x60;null&#x60; if none of their matches has a known region. |  [optional] |
| **regionMonth** | **kotlin.Int** | Unix timestamp of the month &#x60;region&#x60; was taken from. |  [optional] |



