# DeadlockApiClient.Model.ESportsMatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Provider** | **string** | The provider of the match data. Some string that identifies the source of the data. | 
**MatchId** | **long** | Valve&#39;s match id of the match. | [optional] 
**ScheduledDate** | **DateTime** | The scheduled date of the match. | [optional] 
**Status** | **ESportsMatchStatus** | The status of the match, e.g. live, completed, scheduled, cancelled. | [optional] 
**Team0Name** | **string** | The name of the first team. | [optional] 
**Team1Name** | **string** | The name of the second team. | [optional] 
**TournamentName** | **string** | The name of the tournament. | [optional] 
**TournamentStage** | **string** | The stage of the tournament. | [optional] 
**UpdateId** | **Guid** | If you want to update an existing match, you can provide an update id. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

