# DeadlockApiClient.Model.LastRankedMatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MatchId** | **long** |  | 
**PlayerRankInitialDisplayRank** | **int** | Rank badge the player entered the match with, &#x60;tier * 10 + subrank&#x60;. | 
**StartTime** | **int** | Match start time as a unix timestamp. | 
**PlayerRankConsumedDemotionProtection** | **bool** | Whether the match used up one of the player&#39;s demotion protection games. | [optional] 
**PlayerRankDesiredProgressChange** | **int** | Progress change the match was supposed to award, before demotion protection is applied. | [optional] 
**PlayerRankFinalFlatProgress** | **int** | Rank progress the player ended the match with. | [optional] 
**PlayerRankInitialCalibrationGames** | **int** | Remaining placement games at the start of the match. | [optional] 
**PlayerRankInitialDemotionProtectionGames** | **int** | Remaining demotion protection games at the start of the match. | [optional] 
**PlayerRankInitialFlatProgress** | **int** | Rank progress the player entered the match with. | [optional] 
**PlayerRankInitialWinStreak** | **int** | Win streak the player entered the match with. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

