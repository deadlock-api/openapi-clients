
# AnalyticsAbilityOrderTreeNode

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **abilities** | **kotlin.collections.List&lt;kotlin.Int&gt;** | The order prefix: one entry per ability point spent, unlocks included. Its parent node is the prefix one entry shorter. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; |  |
| **avgUpgradeTimeS** | **kotlin.Double** | Average game time (in seconds) at which the last upgrade in &#x60;abilities&#x60; was bought. |  |
| **losses** | **kotlin.Long** |  |  |
| **matches** | **kotlin.Long** |  |  |
| **players** | **kotlin.Long** | Distinct players, counted exactly. |  |
| **totalAssists** | **kotlin.Long** |  |  |
| **totalDeaths** | **kotlin.Long** |  |  |
| **totalKills** | **kotlin.Long** |  |  |
| **wins** | **kotlin.Long** |  |  |



