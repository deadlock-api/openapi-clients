# DeadlockApiClient.Model.PlayerMatchHistoryEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **long** |  | 
**Denies** | **long** |  | 
**GameMode** | **int** |  | 
**HeroId** | **int** | See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**HeroLevel** | **long** |  | 
**LastHits** | **long** |  | 
**MatchDurationS** | **long** |  | 
**MatchId** | **long** |  | 
**MatchMode** | **int** |  | 
**MatchResult** | **long** |  | 
**NetWorth** | **long** |  | 
**ObjectivesMaskTeam0** | **long** |  | 
**ObjectivesMaskTeam1** | **long** |  | 
**PlayerAssists** | **long** |  | 
**PlayerDeaths** | **long** |  | 
**PlayerKills** | **long** |  | 
**PlayerMatchOutcome** | **int** | How the match was scored for the player: 0 &#x3D; invalid, 1 &#x3D; win, 2 &#x3D; loss, 3 &#x3D; penalized, 4 &#x3D; penalized party, 5 &#x3D; not scored. | 
**PlayerTeam** | **int** |  | 
**StartTime** | **long** |  | 
**AbandonedTimeS** | **long** |  | [optional] 
**BrawlAvgRoundTimeS** | **long** |  | [optional] 
**BrawlScoreTeam0** | **long** |  | [optional] 
**BrawlScoreTeam1** | **long** |  | [optional] 
**LowPriPool** | **bool** | Whether the match was played in the low priority pool. &#x60;None&#x60; for entries stored before this was recorded. | [optional] 
**RankedCalibrationMatch** | **long** | Non-zero if this match counted towards the player&#39;s ranked calibration. | [optional] 
**RankedDelta** | **int** | The ranked progress change the player got from this match. | [optional] 
**RankedDisplayBadge** | **long** | The ranked badge shown for the player after the match (tier &#x3D; first digits, subtier &#x3D; last digit). Within Eternus, where subranks are percentile cuts the GC misreports, this is the badge the player entered the match with. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] 
**RankedUsedDemotionProtection** | **bool** | Whether the player&#39;s demotion protection absorbed a loss in this match. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

