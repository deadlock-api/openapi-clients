# deadlock-api-client.model.ESportsMatch

## Load the model package
```dart
import 'package:deadlock-api-client/api.dart';
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matchId** | **int** | Valve's match id of the match. | [optional] 
**provider** | **String** | The provider of the match data. Some string that identifies the source of the data. | 
**scheduledDate** | [**DateTime**](DateTime.md) | The scheduled date of the match. | [optional] 
**status** | [**ESportsMatchStatus**](ESportsMatchStatus.md) | The status of the match, e.g. live, completed, scheduled, cancelled. | [optional] 
**team0Name** | **String** | The name of the first team. | [optional] 
**team1Name** | **String** | The name of the second team. | [optional] 
**tournamentName** | **String** | The name of the tournament. | [optional] 
**tournamentStage** | **String** | The stage of the tournament. | [optional] 
**updateId** | **String** | If you want to update an existing match, you can provide an update id. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


