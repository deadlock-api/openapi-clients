
# LastRankedMatch

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **matchId** | **kotlin.Long** |  |  |
| **playerRankInitialDisplayRank** | **kotlin.Long** | Rank badge the player entered the match with, &#x60;tier * 10 + subrank&#x60;. |  |
| **startTime** | **kotlin.Long** | Match start time as a unix timestamp. |  |
| **playerRankConsumedDemotionProtection** | **kotlin.Boolean** | Whether the match used up one of the player&#39;s demotion protection games. |  [optional] |
| **playerRankDesiredProgressChange** | **kotlin.Int** | Progress change the match was supposed to award, before demotion protection is applied. |  [optional] |
| **playerRankFinalFlatProgress** | **kotlin.Long** | Rank progress the player ended the match with. |  [optional] |
| **playerRankInitialCalibrationGames** | **kotlin.Long** | Remaining placement games at the start of the match. |  [optional] |
| **playerRankInitialDemotionProtectionGames** | **kotlin.Long** | Remaining demotion protection games at the start of the match. |  [optional] |
| **playerRankInitialFlatProgress** | **kotlin.Long** | Rank progress the player entered the match with. |  [optional] |
| **playerRankInitialWinStreak** | **kotlin.Long** | Win streak the player entered the match with. |  [optional] |
| **rankInterval** | **kotlin.Long** | Ranked interval the match counted for, which sets the scale of the flat progress. See &lt;https://api.deadlock-api.com/v1/assets/ranked-seasons&gt;. &#x60;null&#x60; for matches before 2026-11-05 19:00 UTC, which are all interval 1. |  [optional] |



