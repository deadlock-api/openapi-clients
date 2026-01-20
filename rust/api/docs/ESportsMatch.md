# ESportsMatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_id** | Option<**i64**> | Valve's match id of the match. | [optional]
**provider** | **String** | The provider of the match data. Some string that identifies the source of the data. | 
**scheduled_date** | Option<**String**> | The scheduled date of the match. | [optional]
**status** | Option<[**models::ESportsMatchStatus**](ESportsMatchStatus.md)> | The status of the match, e.g. live, completed, scheduled, cancelled. | [optional]
**team0_name** | Option<**String**> | The name of the first team. | [optional]
**team1_name** | Option<**String**> | The name of the second team. | [optional]
**tournament_name** | Option<**String**> | The name of the tournament. | [optional]
**tournament_stage** | Option<**String**> | The stage of the tournament. | [optional]
**update_id** | Option<**uuid::Uuid**> | If you want to update an existing match, you can provide an update id. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


