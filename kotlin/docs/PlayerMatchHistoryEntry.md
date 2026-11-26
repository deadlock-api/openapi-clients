
# PlayerMatchHistoryEntry

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Long** |  |  |
| **denies** | **kotlin.Long** |  |  |
| **gameMode** | **kotlin.Int** |  |  |
| **heroId** | **kotlin.Int** | See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; |  |
| **heroLevel** | **kotlin.Long** |  |  |
| **lastHits** | **kotlin.Long** |  |  |
| **matchDurationS** | **kotlin.Long** |  |  |
| **matchId** | **kotlin.Long** |  |  |
| **matchMode** | **kotlin.Int** |  |  |
| **matchResult** | **kotlin.Long** |  |  |
| **netWorth** | **kotlin.Long** |  |  |
| **objectivesMaskTeam0** | **kotlin.Long** |  |  |
| **objectivesMaskTeam1** | **kotlin.Long** |  |  |
| **playerAssists** | **kotlin.Long** |  |  |
| **playerDeaths** | **kotlin.Long** |  |  |
| **playerKills** | **kotlin.Long** |  |  |
| **playerMatchOutcome** | **kotlin.Int** | How the match was scored for the player: 0 &#x3D; invalid, 1 &#x3D; win, 2 &#x3D; loss, 3 &#x3D; penalized, 4 &#x3D; penalized party, 5 &#x3D; not scored. |  |
| **playerTeam** | **kotlin.Int** |  |  |
| **startTime** | **kotlin.Long** |  |  |
| **abandonedTimeS** | **kotlin.Long** |  |  [optional] |
| **brawlAvgRoundTimeS** | **kotlin.Long** |  |  [optional] |
| **brawlScoreTeam0** | **kotlin.Long** |  |  [optional] |
| **brawlScoreTeam1** | **kotlin.Long** |  |  [optional] |
| **lowPriPool** | **kotlin.Boolean** | Whether the match was played in the low priority pool. &#x60;None&#x60; for entries stored before this was recorded. |  [optional] |
| **rankedCalibrationMatch** | **kotlin.Long** | Non-zero if this match counted towards the player&#39;s ranked calibration. |  [optional] |
| **rankedDelta** | **kotlin.Int** | The ranked progress change the player got from this match. |  [optional] |
| **rankedDisplayBadge** | **kotlin.Long** | The ranked badge shown for the player after the match (tier &#x3D; first digits, subtier &#x3D; last digit). Within Eternus, where subranks are percentile cuts the GC misreports, this is the badge the player entered the match with. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; |  [optional] |
| **rankedUsedDemotionProtection** | **kotlin.Boolean** | Whether the player&#39;s demotion protection absorbed a loss in this match. |  [optional] |



