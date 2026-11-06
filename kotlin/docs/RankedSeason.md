
# RankedSeason

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **calibrationMatches** | **kotlin.Int** |  |  |
| **className** | **kotlin.String** |  |  |
| **intervals** | [**kotlin.collections.List&lt;SeasonInterval&gt;**](SeasonInterval.md) |  |  |
| **minHeroUnlocks** | **kotlin.Int** |  |  |
| **minWins** | **kotlin.Int** |  |  |
| **name** | **kotlin.String** |  |  |
| **rankedType** | **kotlin.String** |  |  |
| **validPartySizes** | **kotlin.collections.List&lt;kotlin.Int&gt;** |  |  |
| **baseWinLossPointGrant** | **kotlin.Int** | Base rank points granted per win / taken per loss (build 6701+). |  [optional] |
| **calibrationMaxRank** | **kotlin.Int** | Highest rank badge (tier * 10 + subrank) placements put a player at (build 6857+). Valve&#39;s notes for Beta Season 2 (101, Ascendant I) allow up to Ascendant III for strong previous-season performance. |  [optional] |
| **minHeroUnlockPoints** | **kotlin.Int** | Points a hero needs to count towards &#x60;min_hero_unlocks&#x60;: 2 per win, 1 per loss (build 6857+). |  [optional] |
| **minHeroWins** | **kotlin.Int** | Wins a hero needs to count towards &#x60;min_hero_unlocks&#x60;. Absent where the season counts hero points instead, see &#x60;min_hero_unlock_points&#x60;. |  [optional] |
| **rankInfo** | [**kotlin.collections.List&lt;RankInfo&gt;**](RankInfo.md) | Rank progression settings (build 6857+). |  [optional] |



