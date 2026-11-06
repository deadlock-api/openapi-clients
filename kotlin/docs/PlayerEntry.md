
# PlayerEntry

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Int** |  |  |
| **matches** | **kotlin.Long** |  |  |
| **rank** | **kotlin.Long** |  |  |
| **&#x60;value&#x60;** | **kotlin.Double** |  |  |
| **badge** | **kotlin.Int** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: the rank badge the progress in &#x60;value&#x60; falls in, &#x60;0&#x60; when the player has no ranked match in range. Omitted for every other sort. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; |  [optional] |
| **badgeProgress** | **kotlin.Int** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: progress points into &#x60;badge&#x60;, out of &#x60;badge_progress_max&#x60;. In Eternus, whose subranks are percentile cuts rather than point spans, the points past the start of Eternus. &#x60;null&#x60; when the player has no ranked match in range. |  [optional] |
| **badgeProgressMax** | **kotlin.Int** | &#x60;rank&#x60; and &#x60;peak_rank&#x60; sorts only: the points the subrank of &#x60;badge&#x60; spans in that match&#39;s season (&#x60;sub_rank_xp&#x60; in &lt;https://api.deadlock-api.com/v1/assets/ranked-seasons&gt;). &#x60;null&#x60; in Eternus and when the player has no ranked match in range. |  [optional] |



