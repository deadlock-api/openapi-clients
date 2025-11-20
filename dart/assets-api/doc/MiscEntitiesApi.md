# assets-deadlock-api-client.api.MiscEntitiesApi

## Load the API package
```dart
import 'package:assets-deadlock-api-client/api.dart';
```

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMiscEntitiesV2MiscEntitiesGet**](MiscEntitiesApi.md#getmiscentitiesv2miscentitiesget) | **GET** /v2/misc-entities | Get Misc Entities
[**getMiscEntityV2MiscEntitiesIdOrClassNameGet**](MiscEntitiesApi.md#getmiscentityv2miscentitiesidorclassnameget) | **GET** /v2/misc-entities/{id_or_class_name} | Get Misc Entity


# **getMiscEntitiesV2MiscEntitiesGet**
> List<MiscV2> getMiscEntitiesV2MiscEntitiesGet(clientVersion)

Get Misc Entities

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = MiscEntitiesApi();
final clientVersion = ; // DeadlockAssetsApiRoutesV1ValidClientVersions | 

try {
    final result = api_instance.getMiscEntitiesV2MiscEntitiesGet(clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling MiscEntitiesApi->getMiscEntitiesV2MiscEntitiesGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesV1ValidClientVersions**](.md)|  | [optional] 

### Return type

[**List<MiscV2>**](MiscV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getMiscEntityV2MiscEntitiesIdOrClassNameGet**
> NPCUnitV2 getMiscEntityV2MiscEntitiesIdOrClassNameGet(idOrClassName, clientVersion)

Get Misc Entity

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = MiscEntitiesApi();
final idOrClassName = idOrClassName_example; // String | 
final clientVersion = ; // DeadlockAssetsApiRoutesV1ValidClientVersions | 

try {
    final result = api_instance.getMiscEntityV2MiscEntitiesIdOrClassNameGet(idOrClassName, clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling MiscEntitiesApi->getMiscEntityV2MiscEntitiesIdOrClassNameGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idOrClassName** | **String**|  | 
 **clientVersion** | [**DeadlockAssetsApiRoutesV1ValidClientVersions**](.md)|  | [optional] 

### Return type

[**NPCUnitV2**](NPCUnitV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

