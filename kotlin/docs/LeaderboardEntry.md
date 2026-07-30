
# LeaderboardEntry

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **accountName** | **kotlin.String** | The account name of the player. |  [optional] |
| **possibleAccountIds** | **kotlin.collections.List&lt;kotlin.Int&gt;** | The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.** |  [optional] |
| **rank** | **kotlin.Int** | The rank of the player (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; |  [optional] |
| **topHeroIds** | **kotlin.collections.List&lt;kotlin.Int&gt;** | The top hero IDs of the player. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; |  [optional] |



