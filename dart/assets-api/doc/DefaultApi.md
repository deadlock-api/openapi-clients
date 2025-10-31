# assets-deadlock-api-client.api.DefaultApi

## Load the API package
```dart
import 'package:assets-deadlock-api-client/api.dart';
```

All URIs are relative to *https://assets.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBuildTagsV2BuildTagsGet**](DefaultApi.md#getbuildtagsv2buildtagsget) | **GET** /v2/build-tags | Get Build Tags
[**getClientVersionsV2ClientVersionsGet**](DefaultApi.md#getclientversionsv2clientversionsget) | **GET** /v2/client-versions | Get Client Versions
[**getColorsV1ColorsGet**](DefaultApi.md#getcolorsv1colorsget) | **GET** /v1/colors | Get Colors
[**getIconsV1IconsGet**](DefaultApi.md#geticonsv1iconsget) | **GET** /v1/icons | Get Icons
[**getMapV1MapGet**](DefaultApi.md#getmapv1mapget) | **GET** /v1/map | Get Map
[**getRanksV2RanksGet**](DefaultApi.md#getranksv2ranksget) | **GET** /v2/ranks | Get Ranks
[**getSoundsV1SoundsGet**](DefaultApi.md#getsoundsv1soundsget) | **GET** /v1/sounds | Get Sounds
[**getSteamInfoV1SteamInfoGet**](DefaultApi.md#getsteaminfov1steaminfoget) | **GET** /v1/steam-info | Get Steam Info


# **getBuildTagsV2BuildTagsGet**
> List<BuildTagV2Output> getBuildTagsV2BuildTagsGet(language, clientVersion)

Get Build Tags

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = DefaultApi();
final language = ; // Language | 
final clientVersion = ; // DeadlockAssetsApiRoutesV1ValidClientVersions | 

try {
    final result = api_instance.getBuildTagsV2BuildTagsGet(language, clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling DefaultApi->getBuildTagsV2BuildTagsGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](.md)|  | [optional] 
 **clientVersion** | [**DeadlockAssetsApiRoutesV1ValidClientVersions**](.md)|  | [optional] 

### Return type

[**List<BuildTagV2Output>**](BuildTagV2Output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getClientVersionsV2ClientVersionsGet**
> List<int> getClientVersionsV2ClientVersionsGet()

Get Client Versions

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = DefaultApi();

try {
    final result = api_instance.getClientVersionsV2ClientVersionsGet();
    print(result);
} catch (e) {
    print('Exception when calling DefaultApi->getClientVersionsV2ClientVersionsGet: $e\n');
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List<int>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getColorsV1ColorsGet**
> Map<String, ColorV1> getColorsV1ColorsGet(clientVersion)

Get Colors

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = DefaultApi();
final clientVersion = ; // DeadlockAssetsApiRoutesV1ValidClientVersions | 

try {
    final result = api_instance.getColorsV1ColorsGet(clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling DefaultApi->getColorsV1ColorsGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesV1ValidClientVersions**](.md)|  | [optional] 

### Return type

[**Map<String, ColorV1>**](ColorV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getIconsV1IconsGet**
> Map<String, String> getIconsV1IconsGet(clientVersion)

Get Icons

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = DefaultApi();
final clientVersion = ; // DeadlockAssetsApiRoutesV1ValidClientVersions | 

try {
    final result = api_instance.getIconsV1IconsGet(clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling DefaultApi->getIconsV1IconsGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesV1ValidClientVersions**](.md)|  | [optional] 

### Return type

**Map<String, String>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getMapV1MapGet**
> MapV1 getMapV1MapGet(clientVersion)

Get Map

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = DefaultApi();
final clientVersion = ; // DeadlockAssetsApiRoutesV1ValidClientVersions | 

try {
    final result = api_instance.getMapV1MapGet(clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling DefaultApi->getMapV1MapGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesV1ValidClientVersions**](.md)|  | [optional] 

### Return type

[**MapV1**](MapV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getRanksV2RanksGet**
> List<RankV2Output> getRanksV2RanksGet(language, clientVersion)

Get Ranks

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = DefaultApi();
final language = ; // Language | 
final clientVersion = ; // DeadlockAssetsApiRoutesV1ValidClientVersions | 

try {
    final result = api_instance.getRanksV2RanksGet(language, clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling DefaultApi->getRanksV2RanksGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**Language**](.md)|  | [optional] 
 **clientVersion** | [**DeadlockAssetsApiRoutesV1ValidClientVersions**](.md)|  | [optional] 

### Return type

[**List<RankV2Output>**](RankV2Output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getSoundsV1SoundsGet**
> Map<String, Object> getSoundsV1SoundsGet(clientVersion)

Get Sounds

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = DefaultApi();
final clientVersion = ; // DeadlockAssetsApiRoutesV1ValidClientVersions | 

try {
    final result = api_instance.getSoundsV1SoundsGet(clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling DefaultApi->getSoundsV1SoundsGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesV1ValidClientVersions**](.md)|  | [optional] 

### Return type

[**Map<String, Object>**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getSteamInfoV1SteamInfoGet**
> Object getSteamInfoV1SteamInfoGet(clientVersion)

Get Steam Info

### Example
```dart
import 'package:assets-deadlock-api-client/api.dart';

final api_instance = DefaultApi();
final clientVersion = ; // DeadlockAssetsApiRoutesV1ValidClientVersions | 

try {
    final result = api_instance.getSteamInfoV1SteamInfoGet(clientVersion);
    print(result);
} catch (e) {
    print('Exception when calling DefaultApi->getSteamInfoV1SteamInfoGet: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientVersion** | [**DeadlockAssetsApiRoutesV1ValidClientVersions**](.md)|  | [optional] 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

