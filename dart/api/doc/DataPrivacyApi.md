# deadlock-api-client.api.DataPrivacyApi

## Load the API package
```dart
import 'package:deadlock-api-client/api.dart';
```

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**requestDeletion**](DataPrivacyApi.md#requestdeletion) | **POST** /v1/data-privacy/request-deletion | Request Data Deletion
[**requestTracking**](DataPrivacyApi.md#requesttracking) | **POST** /v1/data-privacy/request-tracking | Request Data Tracking


# **requestDeletion**
> requestDeletion(dataPrivacyRequest)

Request Data Deletion

 Endpoint to request deletion of personal data.     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = DataPrivacyApi();
final dataPrivacyRequest = DataPrivacyRequest(); // DataPrivacyRequest | 

try {
    api_instance.requestDeletion(dataPrivacyRequest);
} catch (e) {
    print('Exception when calling DataPrivacyApi->requestDeletion: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataPrivacyRequest** | [**DataPrivacyRequest**](DataPrivacyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requestTracking**
> requestTracking(dataPrivacyRequest)

Request Data Tracking

 Endpoint to request tracking of personal data.  Use this to opt back into data tracking after previously requesting deletion.     

### Example
```dart
import 'package:deadlock-api-client/api.dart';

final api_instance = DataPrivacyApi();
final dataPrivacyRequest = DataPrivacyRequest(); // DataPrivacyRequest | 

try {
    api_instance.requestTracking(dataPrivacyRequest);
} catch (e) {
    print('Exception when calling DataPrivacyApi->requestTracking: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataPrivacyRequest** | [**DataPrivacyRequest**](DataPrivacyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

