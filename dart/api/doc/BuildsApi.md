# deadlock-api-client.api.BuildsApi

## Load the API package
```dart
import 'package:deadlock-api-client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchBuilds**](BuildsApi.md#searchbuilds) | **GET** /v1/builds | Search


# **searchBuilds**
> List<Build> searchBuilds(minUnixTimestamp, maxUnixTimestamp, minPublishedUnixTimestamp, maxPublishedUnixTimestamp, sortBy, start, limit, sortDirection, searchName, searchDescription, onlyLatest, language, buildId, version, heroId, tag, rollupCategory, authorId)

Search

 Search for builds based on various criteria.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = BuildsApi();
final minUnixTimestamp = 789; // int | Filter builds based on their `last_updated` time (Unix timestamp).
final maxUnixTimestamp = 789; // int | Filter builds based on their `last_updated` time (Unix timestamp).
final minPublishedUnixTimestamp = 789; // int | Filter builds based on their published time (Unix timestamp).
final maxPublishedUnixTimestamp = 789; // int | Filter builds based on their published time (Unix timestamp).
final sortBy = sortBy_example; // String | The field to sort the builds by.
final start = 56; // int | The index of the first build to return.
final limit = 56; // int | The maximum number of builds to return.
final sortDirection = sortDirection_example; // String | The direction to sort the builds in.
final searchName = searchName_example; // String | Search for builds with a name containing this string.
final searchDescription = searchDescription_example; // String | Search for builds with a description containing this string.
final onlyLatest = true; // bool | Only return the latest version of each build.
final language = 56; // int | Filter builds by language.
final buildId = 56; // int | Filter builds by ID.
final version = 56; // int | Filter builds by version.
final heroId = 56; // int | Filter builds by hero ID. See more: <https://assets.deadlock-api.com/v2/heroes>
final tag = 56; // int | Filter builds by tag.
final rollupCategory = 56; // int | Filter builds by rollup category.
final authorId = 56; // int | The author's `SteamID3`

try {
    final result = api_instance.searchBuilds(minUnixTimestamp, maxUnixTimestamp, minPublishedUnixTimestamp, maxPublishedUnixTimestamp, sortBy, start, limit, sortDirection, searchName, searchDescription, onlyLatest, language, buildId, version, heroId, tag, rollupCategory, authorId);
    print(result);
} catch (e) {
    print('Exception when calling BuildsApi->searchBuilds: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minUnixTimestamp** | **int**| Filter builds based on their `last_updated` time (Unix timestamp). | [optional] 
 **maxUnixTimestamp** | **int**| Filter builds based on their `last_updated` time (Unix timestamp). | [optional] 
 **minPublishedUnixTimestamp** | **int**| Filter builds based on their published time (Unix timestamp). | [optional] 
 **maxPublishedUnixTimestamp** | **int**| Filter builds based on their published time (Unix timestamp). | [optional] 
 **sortBy** | **String**| The field to sort the builds by. | [optional] 
 **start** | **int**| The index of the first build to return. | [optional] 
 **limit** | **int**| The maximum number of builds to return. | [optional] [default to 100]
 **sortDirection** | **String**| The direction to sort the builds in. | [optional] 
 **searchName** | **String**| Search for builds with a name containing this string. | [optional] 
 **searchDescription** | **String**| Search for builds with a description containing this string. | [optional] 
 **onlyLatest** | **bool**| Only return the latest version of each build. | [optional] 
 **language** | **int**| Filter builds by language. | [optional] 
 **buildId** | **int**| Filter builds by ID. | [optional] 
 **version** | **int**| Filter builds by version. | [optional] 
 **heroId** | **int**| Filter builds by hero ID. See more: <https://assets.deadlock-api.com/v2/heroes> | [optional] 
 **tag** | **int**| Filter builds by tag. | [optional] 
 **rollupCategory** | **int**| Filter builds by rollup category. | [optional] 
 **authorId** | **int**| The author's `SteamID3` | [optional] 

### Return type

[**List<Build>**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

