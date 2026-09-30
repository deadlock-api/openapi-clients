
# PlayerEntry

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Int** |  |  |
| **matches** | **kotlin.Long** |  |  |
| **rank** | **kotlin.Long** |  |  |
| **&#x60;value&#x60;** | **kotlin.Double** |  |  |
| **badge** | **kotlin.Int** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: the rank badge the progress in &#x60;value&#x60; falls in, &#x60;0&#x60; when the player has no ranked match in range. Omitted for every other sort. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; |  [optional] |
| **badgeProgress** | **kotlin.Int** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: progress points into &#x60;badge&#x60;. A subrank spans 1000 points, the sixth of a tier 2000. &#x60;null&#x60; in Eternus, whose subranks are percentile cuts rather than point spans, and when the player has no ranked match in range. |  [optional] |



