# deadlock_api_client.api.PatchesApi

## Load the API package
```dart
import 'package:deadlock_api_client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bigPatchDays**](PatchesApi.md#bigpatchdays) | **GET** /v1/patches/big-days | Big Days
[**feed**](PatchesApi.md#feed) | **GET** /v1/patches | Notes


# **bigPatchDays**
> List<String> bigPatchDays()

Big Days

 Returns a list of dates where Deadlock's \"big\" patch days were, usually bi-weekly. The exact date is the time when the announcement forum post was published.  This list is manually maintained, and so new patch dates may be delayed by a few hours.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock_api_client/api.dart';

final api_instance = PatchesApi();

try {
    final result = api_instance.bigPatchDays();
    print(result);
} catch (e) {
    print('Exception when calling PatchesApi->bigPatchDays: $e\n');
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List<String>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feed**
> List<ModelPatch> feed()

Notes

 Returns the parsed result of the RSS Feed from the official Forum.  RSS-Feed: https://forums.playdeadlock.com/forums/changelog.10/index.rss  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock_api_client/api.dart';

final api_instance = PatchesApi();

try {
    final result = api_instance.feed();
    print(result);
} catch (e) {
    print('Exception when calling PatchesApi->feed: $e\n');
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List<ModelPatch>**](ModelPatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

