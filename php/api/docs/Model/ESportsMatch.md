# # ESportsMatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_id** | **int** | Valve&#39;s match id of the match. | [optional]
**provider** | **string** | The provider of the match data. Some string that identifies the source of the data. |
**scheduled_date** | **\DateTime** | The scheduled date of the match. | [optional]
**status** | [**\OpenAPI\Client\Model\ESportsMatchStatus**](ESportsMatchStatus.md) | The status of the match, e.g. live, completed, scheduled, cancelled. | [optional]
**team0_name** | **string** | The name of the first team. | [optional]
**team1_name** | **string** | The name of the second team. | [optional]
**tournament_name** | **string** | The name of the tournament. | [optional]
**tournament_stage** | **string** | The stage of the tournament. | [optional]
**update_id** | **string** | If you want to update an existing match, you can provide an update id. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
