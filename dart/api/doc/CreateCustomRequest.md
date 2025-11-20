# deadlock_api_client.model.CreateCustomRequest

## Load the model package
```dart
import 'package:deadlock_api_client/api.dart';
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callbackUrl** | **String** | If a callback url is provided, we will send a POST request to this url when the match starts. | [optional] 
**cheatsEnabled** | **bool** |  | [optional] 
**disableAutoReady** | **bool** | If auto-ready is disabled, the bot will not automatically ready up. You need to call the `ready` endpoint to ready up. | [optional] 
**duplicateHeroesEnabled** | **bool** |  | [optional] 
**experimentalHeroesEnabled** | **bool** |  | [optional] 
**isPubliclyVisible** | **bool** |  | [optional] 
**minRosterSize** | **int** |  | [optional] 
**randomizeLanes** | **bool** |  | [optional] 
**regionMode** | [**RegionMode**](RegionMode.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


