# assets_deadlock_api_client.api.ItemsApi

## Load the API package
```dart
import 'package:assets_deadlock_api_client/api.dart';
```

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getItemV2ItemsIdOrClassNameGet**](ItemsApi.md#getitemv2itemsidorclassnameget) | **GET** /v2/items/{id_or_class_name} | Get Item
[**getItemsByHeroIdV2ItemsByHeroIdIdGet**](ItemsApi.md#getitemsbyheroidv2itemsbyheroididget) | **GET** /v2/items/by-hero-id/{id} | Get Items By Hero Id
[**getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet**](ItemsApi.md#getitemsbyslottypev2itemsbyslottypeslottypeget) | **GET** /v2/items/by-slot-type/{slot_type} | Get Items By Slot Type
[**getItemsByTypeV2ItemsByTypeTypeGet**](ItemsApi.md#getitemsbytypev2itemsbytypetypeget) | **GET** /v2/items/by-type/{type} | Get Items By Type
[**getItemsV2ItemsGet**](ItemsApi.md#getitemsv2itemsget) | **GET** /v2/items | Get Items


# **getItemV2ItemsIdOrClassNameGet**
> ResponseGetItemV2ItemsIdOrClassNameGet getItemV2ItemsIdOrClassNameGet(idOrClassName, language, clientVersion)

Get Item

### Example
```dart
import 'package:assets_deadlock_api_client/api.dart';

final api_instance = ItemsApi();
final idOrClassName = idOrClassName_example; // String | 
final language = ; // Language | 
final clientVersion = ; // DeadlockAssetsApiRoutesV2ValidClientVersions | 

try {
    final result = api_instance.getItemV2ItemsIdOrClassNameGet(idOrClassName, language, clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling ItemsApi->getItemV2ItemsIdOrClassNameGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idOrClassName** | **String**|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 

### Return type

[**ResponseGetItemV2ItemsIdOrClassNameGet**](ResponseGetItemV2ItemsIdOrClassNameGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getItemsByHeroIdV2ItemsByHeroIdIdGet**
> List<GetItemsV2ItemsGet200ResponseInner> getItemsByHeroIdV2ItemsByHeroIdIdGet(id, language, clientVersion)

Get Items By Hero Id

### Example
```dart
import 'package:assets_deadlock_api_client/api.dart';

final api_instance = ItemsApi();
final id = 56; // int | 
final language = ; // Language | 
final clientVersion = ; // DeadlockAssetsApiRoutesV2ValidClientVersions | 

try {
    final result = api_instance.getItemsByHeroIdV2ItemsByHeroIdIdGet(id, language, clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling ItemsApi->getItemsByHeroIdV2ItemsByHeroIdIdGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 

### Return type

[**List<GetItemsV2ItemsGet200ResponseInner>**](GetItemsV2ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet**
> List<GetItemsV2ItemsGet200ResponseInner> getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet(slotType, language, clientVersion)

Get Items By Slot Type

### Example
```dart
import 'package:assets_deadlock_api_client/api.dart';

final api_instance = ItemsApi();
final slotType = ; // ItemSlotTypeV2 | 
final language = ; // Language | 
final clientVersion = ; // DeadlockAssetsApiRoutesV2ValidClientVersions | 

try {
    final result = api_instance.getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet(slotType, language, clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling ItemsApi->getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slotType** | [**ItemSlotTypeV2**](.md)|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 

### Return type

[**List<GetItemsV2ItemsGet200ResponseInner>**](GetItemsV2ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getItemsByTypeV2ItemsByTypeTypeGet**
> List<GetItemsV2ItemsGet200ResponseInner> getItemsByTypeV2ItemsByTypeTypeGet(type, language, clientVersion)

Get Items By Type

### Example
```dart
import 'package:assets_deadlock_api_client/api.dart';

final api_instance = ItemsApi();
final type = ; // ItemTypeV2 | 
final language = ; // Language | 
final clientVersion = ; // DeadlockAssetsApiRoutesV2ValidClientVersions | 

try {
    final result = api_instance.getItemsByTypeV2ItemsByTypeTypeGet(type, language, clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling ItemsApi->getItemsByTypeV2ItemsByTypeTypeGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**ItemTypeV2**](.md)|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 

### Return type

[**List<GetItemsV2ItemsGet200ResponseInner>**](GetItemsV2ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getItemsV2ItemsGet**
> List<GetItemsV2ItemsGet200ResponseInner> getItemsV2ItemsGet(language, clientVersion)

Get Items

### Example
```dart
import 'package:assets_deadlock_api_client/api.dart';

final api_instance = ItemsApi();
final language = ; // Language | 
final clientVersion = ; // DeadlockAssetsApiRoutesV2ValidClientVersions | 

try {
    final result = api_instance.getItemsV2ItemsGet(language, clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling ItemsApi->getItemsV2ItemsGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](.md)|  | [optional] 
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 

### Return type

[**List<GetItemsV2ItemsGet200ResponseInner>**](GetItemsV2ItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

