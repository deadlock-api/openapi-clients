# deadlock-api-client.api.InfoApi

## Load the API package
```dart
import 'package:deadlock-api-client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthCheck**](InfoApi.md#healthcheck) | **GET** /v1/info/health | Health Check
[**info**](InfoApi.md#info) | **GET** /v1/info | API Info


# **healthCheck**
> Status healthCheck()

Health Check

 Checks the health of the services.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = InfoApi();

try {
    final result = api_instance.healthCheck();
    print(result);
} catch (e) {
    print('Exception when calling InfoApi->healthCheck: $e\n');
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info**
> APIInfo info()

API Info

 Returns information about the API.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = InfoApi();

try {
    final result = api_instance.info();
    print(result);
} catch (e) {
    print('Exception when calling InfoApi->info: $e\n');
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIInfo**](APIInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

