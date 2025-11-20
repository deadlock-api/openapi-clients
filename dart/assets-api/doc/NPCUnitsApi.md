# assets-deadlock-api-client.api.NPCUnitsApi

## Load the API package
```dart
import 'package:assets-deadlock-api-client/api.dart';
```

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNpcUnitV2NpcUnitsIdOrClassNameGet**](NPCUnitsApi.md#getnpcunitv2npcunitsidorclassnameget) | **GET** /v2/npc-units/{id_or_class_name} | Get Npc Unit
[**getNpcUnitsV2NpcUnitsGet**](NPCUnitsApi.md#getnpcunitsv2npcunitsget) | **GET** /v2/npc-units | Get Npc Units


# **getNpcUnitV2NpcUnitsIdOrClassNameGet**
> NPCUnitV2 getNpcUnitV2NpcUnitsIdOrClassNameGet(idOrClassName, clientVersion)

Get Npc Unit

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = NPCUnitsApi();
final idOrClassName = idOrClassName_example; // String | 
final clientVersion = ; // DeadlockAssetsApiRoutesV1ValidClientVersions | 

try {
    final result = api_instance.getNpcUnitV2NpcUnitsIdOrClassNameGet(idOrClassName, clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling NPCUnitsApi->getNpcUnitV2NpcUnitsIdOrClassNameGet: $e\n');
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

# **getNpcUnitsV2NpcUnitsGet**
> List<NPCUnitV2> getNpcUnitsV2NpcUnitsGet(clientVersion)

Get Npc Units

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = NPCUnitsApi();
final clientVersion = ; // DeadlockAssetsApiRoutesV1ValidClientVersions | 

try {
    final result = api_instance.getNpcUnitsV2NpcUnitsGet(clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling NPCUnitsApi->getNpcUnitsV2NpcUnitsGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesV1ValidClientVersions**](.md)|  | [optional] 

### Return type

[**List<NPCUnitV2>**](NPCUnitV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

