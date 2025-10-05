# deadlock-api-client.model.LeaderboardEntry

## Load the model package
```dart
import 'package:deadlock-api-client/api.dart';
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountName** | **String** | The account name of the player. | [optional] 
**badgeLevel** | **int** | The badge level of the player. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
**possibleAccountIds** | **List<int>** | The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.** | [optional] [default to const []]
**rank** | **int** | The rank of the player. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
**rankedRank** | **int** | The ranked rank of the player. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
**rankedSubrank** | **int** | The ranked subrank of the player. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional] 
**topHeroIds** | **List<int>** | The top hero IDs of the player. See more: <https://assets.deadlock-api.com/v2/heroes> | [optional] [default to const []]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


