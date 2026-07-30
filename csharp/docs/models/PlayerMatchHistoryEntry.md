# DeadlockApiClient.Model.PlayerMatchHistoryEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int** |  | 
**Denies** | **int** |  | 
**GameMode** | **int** |  | 
**HeroId** | **int** | See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**HeroLevel** | **int** |  | 
**LastHits** | **int** |  | 
**MatchDurationS** | **int** |  | 
**MatchId** | **long** |  | 
**MatchMode** | **int** |  | 
**MatchResult** | **int** |  | 
**NetWorth** | **int** |  | 
**ObjectivesMaskTeam0** | **int** |  | 
**ObjectivesMaskTeam1** | **int** |  | 
**PlayerAssists** | **int** |  | 
**PlayerDeaths** | **int** |  | 
**PlayerKills** | **int** |  | 
**PlayerMatchOutcome** | **int** | How the match was scored for the player: 0 &#x3D; invalid, 1 &#x3D; win, 2 &#x3D; loss, 3 &#x3D; penalized, 4 &#x3D; penalized party, 5 &#x3D; not scored. | 
**PlayerTeam** | **int** |  | 
**StartTime** | **int** |  | 
**AbandonedTimeS** | **int** |  | [optional] 
**BrawlAvgRoundTimeS** | **int** |  | [optional] 
**BrawlScoreTeam0** | **int** |  | [optional] 
**BrawlScoreTeam1** | **int** |  | [optional] 
**RankedCalibrationMatch** | **int** | Non-zero if this match counted towards the player&#39;s ranked calibration. | [optional] 
**RankedDelta** | **int** | The ranked progress change the player got from this match. | [optional] 
**RankedDisplayBadge** | **int** | The ranked badge shown for the player after the match (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional] 
**RankedUsedDemotionProtection** | **bool** | Whether the player&#39;s demotion protection absorbed a loss in this match. | [optional] 
**TeamAbandoned** | **bool** |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

