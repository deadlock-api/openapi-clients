# assets-deadlock-api-client.api.RawApi

## Load the API package
```dart
import 'package:assets-deadlock-api-client/api.dart';
```

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getGenericDataRawGenericDataGet**](RawApi.md#getgenericdatarawgenericdataget) | **GET** /raw/generic_data | Get Generic Data
[**getRawHeroesRawHeroesGet**](RawApi.md#getrawheroesrawheroesget) | **GET** /raw/heroes | Get Raw Heroes
[**getRawItemsRawItemsGet**](RawApi.md#getrawitemsrawitemsget) | **GET** /raw/items | Get Raw Items


# **getGenericDataRawGenericDataGet**
> Object getGenericDataRawGenericDataGet(clientVersion)

Get Generic Data

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = RawApi();
final clientVersion = ; // DeadlockAssetsApiRoutesRawValidClientVersions | 

try {
    final result = api_instance.getGenericDataRawGenericDataGet(clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling RawApi->getGenericDataRawGenericDataGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesRawValidClientVersions**](.md)|  | [optional] 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getRawHeroesRawHeroesGet**
> Object getRawHeroesRawHeroesGet(clientVersion)

Get Raw Heroes

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = RawApi();
final clientVersion = ; // DeadlockAssetsApiRoutesRawValidClientVersions | 

try {
    final result = api_instance.getRawHeroesRawHeroesGet(clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling RawApi->getRawHeroesRawHeroesGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesRawValidClientVersions**](.md)|  | [optional] 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getRawItemsRawItemsGet**
> Object getRawItemsRawItemsGet(clientVersion)

Get Raw Items

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = RawApi();
final clientVersion = ; // DeadlockAssetsApiRoutesRawValidClientVersions | 

try {
    final result = api_instance.getRawItemsRawItemsGet(clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling RawApi->getRawItemsRawItemsGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesRawValidClientVersions**](.md)|  | [optional] 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

