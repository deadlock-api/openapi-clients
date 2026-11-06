# DeadlockApiClient.Model.RankedSeason

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CalibrationMatches** | **int** |  | 
**ClassName** | **string** |  | 
**Intervals** | [**List&lt;SeasonInterval&gt;**](SeasonInterval.md) |  | 
**MinHeroUnlocks** | **int** |  | 
**MinWins** | **int** |  | 
**Name** | **string** |  | 
**RankedType** | **string** |  | 
**ValidPartySizes** | **List&lt;int&gt;** |  | 
**BaseWinLossPointGrant** | **int** | Base rank points granted per win / taken per loss (build 6701+). | [optional] 
**CalibrationMaxRank** | **int** | Highest rank badge (tier * 10 + subrank) placements put a player at (build 6857+). Valve&#39;s notes for Beta Season 2 (101, Ascendant I) allow up to Ascendant III for strong previous-season performance. | [optional] 
**MinHeroUnlockPoints** | **int** | Points a hero needs to count towards &#x60;min_hero_unlocks&#x60;: 2 per win, 1 per loss (build 6857+). | [optional] 
**MinHeroWins** | **int** | Wins a hero needs to count towards &#x60;min_hero_unlocks&#x60;. Absent where the season counts hero points instead, see &#x60;min_hero_unlock_points&#x60;. | [optional] 
**RankInfo** | [**List&lt;RankInfo&gt;**](RankInfo.md) | Rank progression settings (build 6857+). | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

