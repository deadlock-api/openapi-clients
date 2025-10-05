# deadlock-api-client.api.ESportsApi

## Load the API package
```dart
import 'package:deadlock-api-client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingestMatch**](ESportsApi.md#ingestmatch) | **POST** /v1/esports/ingest/match | Ingest
[**matches**](ESportsApi.md#matches) | **GET** /v1/esports/matches | List Matches


# **ingestMatch**
> ingestMatch(eSportsMatch)

Ingest

 To use this Endpoint you need to have special permissions. Please contact us if you organize E-Sports Matches and want to ingest them to us.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 1000req/h | | Key | - | | Global | 10000req/h |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = ESportsApi();
final eSportsMatch = ESportsMatch(); // ESportsMatch | 

try {
    api_instance.ingestMatch(eSportsMatch);
} catch (e) {
    print('Exception when calling ESportsApi->ingestMatch: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eSportsMatch** | [**ESportsMatch**](ESportsMatch.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matches**
> List<ESportsMatch> matches()

List Matches

 ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = ESportsApi();

try {
    final result = api_instance.matches();
    print(result);
} catch (e) {
    print('Exception when calling ESportsApi->matches: $e\n');
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List<ESportsMatch>**](ESportsMatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

