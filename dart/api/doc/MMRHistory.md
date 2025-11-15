# deadlock-api-client.model.MMRHistory

## Load the model package
```dart
import 'package:deadlock-api-client/api.dart';
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **int** |  | 
**division** | **int** | Extracted from the rank the division (rank // 10) | 
**divisionTier** | **int** | Extracted from the rank the division tier (rank % 10) | 
**matchId** | **int** |  | 
**playerScore** | **double** | Player Score is the index for the rank array (internally used for the rank regression) | 
**rank** | **int** | The Player Rank (tier = first digits, subtier = last digit). See more: <https://assets.deadlock-api.com/v2/ranks> | 
**startTime** | **int** | Start time of the match | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


