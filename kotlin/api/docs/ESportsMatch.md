
# ESportsMatch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **kotlin.String** | The provider of the match data. Some string that identifies the source of the data. | 
**matchId** | **kotlin.Long** | Valve&#39;s match id of the match. |  [optional]
**scheduledDate** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) | The scheduled date of the match. |  [optional]
**status** | [**ESportsMatchStatus**](ESportsMatchStatus.md) | The status of the match, e.g. live, completed, scheduled, cancelled. |  [optional]
**team0Name** | **kotlin.String** | The name of the first team. |  [optional]
**team1Name** | **kotlin.String** | The name of the second team. |  [optional]
**tournamentName** | **kotlin.String** | The name of the tournament. |  [optional]
**tournamentStage** | **kotlin.String** | The stage of the tournament. |  [optional]
**updateId** | [**java.util.UUID**](java.util.UUID.md) | If you want to update an existing match, you can provide an update id. |  [optional]



