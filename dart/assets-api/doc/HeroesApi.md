# assets_deadlock_api_client.api.HeroesApi

## Load the API package
```dart
import 'package:assets_deadlock_api_client/api.dart';
```

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHeroByNameV2HeroesByNameNameGet**](HeroesApi.md#getherobynamev2heroesbynamenameget) | **GET** /v2/heroes/by-name/{name} | Get Hero By Name
[**getHeroV2HeroesIdGet**](HeroesApi.md#getherov2heroesidget) | **GET** /v2/heroes/{id} | Get Hero
[**getHeroesV2HeroesGet**](HeroesApi.md#getheroesv2heroesget) | **GET** /v2/heroes | Get Heroes


# **getHeroByNameV2HeroesByNameNameGet**
> HeroV2 getHeroByNameV2HeroesByNameNameGet(name, language, clientVersion)

Get Hero By Name

### Example
```dart
import 'package:assets_deadlock_api_client/api.dart';

final api_instance = HeroesApi();
final name = name_example; // String | 
final language = ; // Language | 
final clientVersion = ; // DeadlockAssetsApiRoutesV2ValidClientVersions | 

try {
    final result = api_instance.getHeroByNameV2HeroesByNameNameGet(name, language, clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling HeroesApi->getHeroByNameV2HeroesByNameNameGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 

### Return type

[**HeroV2**](HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getHeroV2HeroesIdGet**
> HeroV2 getHeroV2HeroesIdGet(id, language, clientVersion)

Get Hero

### Example
```dart
import 'package:assets_deadlock_api_client/api.dart';

final api_instance = HeroesApi();
final id = 56; // int | 
final language = ; // Language | 
final clientVersion = ; // DeadlockAssetsApiRoutesV2ValidClientVersions | 

try {
    final result = api_instance.getHeroV2HeroesIdGet(id, language, clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling HeroesApi->getHeroV2HeroesIdGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **language** | [**Language**](.md)|  | [optional] 
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 

### Return type

[**HeroV2**](HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getHeroesV2HeroesGet**
> List<HeroV2> getHeroesV2HeroesGet(language, clientVersion, onlyActive)

Get Heroes

### Example
```dart
import 'package:assets_deadlock_api_client/api.dart';

final api_instance = HeroesApi();
final language = ; // Language | 
final clientVersion = ; // DeadlockAssetsApiRoutesV2ValidClientVersions | 
final onlyActive = true; // bool | 

try {
    final result = api_instance.getHeroesV2HeroesGet(language, clientVersion, onlyActive);
    print(result);
} catch (e) {
    print('Exception when calling HeroesApi->getHeroesV2HeroesGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](.md)|  | [optional] 
 **clientVersion** | [**DeadlockAssetsApiRoutesV2ValidClientVersions**](.md)|  | [optional] 
 **onlyActive** | **bool**|  | [optional] 

### Return type

[**List<HeroV2>**](HeroV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

