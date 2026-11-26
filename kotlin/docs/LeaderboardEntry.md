
# LeaderboardEntry

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **possibleAccountIds** | **kotlin.collections.List&lt;kotlin.Long&gt;** | The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.** |  |
| **topHeroIds** | **kotlin.collections.List&lt;kotlin.Long&gt;** | The top hero IDs of the player, as the game sends them. Since 2026-07-31 the game leaves them empty for about half of the entries. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; |  |
| **accountName** | **kotlin.String** | The account name of the player. |  [optional] |
| **rank** | **kotlin.Long** | The player&#39;s place on the leaderboard, starting at 1. Players can share a place, and the following places are then skipped (1, 2, 2, 4). Not a rank badge. |  [optional] |



