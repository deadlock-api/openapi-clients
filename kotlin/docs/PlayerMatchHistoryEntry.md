
# PlayerMatchHistoryEntry

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Int** |  |  |
| **denies** | **kotlin.Int** |  |  |
| **gameMode** | **kotlin.Int** |  |  |
| **heroId** | **kotlin.Int** | See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; |  |
| **heroLevel** | **kotlin.Int** |  |  |
| **lastHits** | **kotlin.Int** |  |  |
| **matchDurationS** | **kotlin.Int** |  |  |
| **matchId** | **kotlin.Long** |  |  |
| **matchMode** | **kotlin.Int** |  |  |
| **matchResult** | **kotlin.Int** |  |  |
| **netWorth** | **kotlin.Int** |  |  |
| **objectivesMaskTeam0** | **kotlin.Int** |  |  |
| **objectivesMaskTeam1** | **kotlin.Int** |  |  |
| **playerAssists** | **kotlin.Int** |  |  |
| **playerDeaths** | **kotlin.Int** |  |  |
| **playerKills** | **kotlin.Int** |  |  |
| **playerMatchOutcome** | **kotlin.Int** | How the match was scored for the player: 0 &#x3D; invalid, 1 &#x3D; win, 2 &#x3D; loss, 3 &#x3D; penalized, 4 &#x3D; penalized party, 5 &#x3D; not scored. |  |
| **playerTeam** | **kotlin.Int** |  |  |
| **startTime** | **kotlin.Int** |  |  |
| **abandonedTimeS** | **kotlin.Int** |  |  [optional] |
| **brawlAvgRoundTimeS** | **kotlin.Int** |  |  [optional] |
| **brawlScoreTeam0** | **kotlin.Int** |  |  [optional] |
| **brawlScoreTeam1** | **kotlin.Int** |  |  [optional] |
| **rankedCalibrationMatch** | **kotlin.Int** | Non-zero if this match counted towards the player&#39;s ranked calibration. |  [optional] |
| **rankedDelta** | **kotlin.Int** | The ranked progress change the player got from this match. |  [optional] |
| **rankedDisplayBadge** | **kotlin.Int** | The ranked badge shown for the player after the match (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; |  [optional] |
| **rankedUsedDemotionProtection** | **kotlin.Boolean** | Whether the player&#39;s demotion protection absorbed a loss in this match. |  [optional] |
| **teamAbandoned** | **kotlin.Boolean** |  |  [optional] |



