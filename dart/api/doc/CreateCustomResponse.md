# deadlock-api-client.model.CreateCustomResponse

## Load the model package
```dart
import 'package:deadlock-api-client/api.dart';
```

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callbackSecret** | **String** | If a callback url is provided, this is the secret that should be used to verify the callback. The secret is a base64 encoded random string. To verify it you should compare it with the X-Callback-Secret header. If no callback url is provided, this will be None. | [optional] 
**partyCode** | **String** |  | 
**partyId** | **String** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


