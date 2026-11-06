
# RankInfo

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **badgeShields** | **kotlin.Int** | Losses a player at a badge&#39;s first subrank with 0 rank points can take before dropping a badge (rank loss protection shields). |  [optional] |
| **rankEnd** | **kotlin.Int** | Rank badge (tier * 10 + subrank) the entry stops at: it covers the ranks below it. In Beta Season 2, 91 (Phantom I) gives every rank below Phantom shields and Phantom and up none. |  [optional] |
| **subRankShields** | **kotlin.Int** | Losses a player can take before dropping a subrank (rank loss protection shields). |  [optional] |
| **subRankXp** | **kotlin.collections.List&lt;kotlin.Int&gt;** | Rank points needed per subrank step, the last one being the step to the next badge (Beta Season 2: 1000 between subranks, 1500 from the final subrank). |  [optional] |



