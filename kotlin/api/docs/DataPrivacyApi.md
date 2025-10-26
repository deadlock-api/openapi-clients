# DataPrivacyApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**requestDeletion**](DataPrivacyApi.md#requestDeletion) | **POST** /v1/data-privacy/request-deletion | Request Data Deletion |
| [**requestTracking**](DataPrivacyApi.md#requestTracking) | **POST** /v1/data-privacy/request-tracking | Request Data Tracking |


<a id="requestDeletion"></a>
# **requestDeletion**
> requestDeletion(dataPrivacyRequest)

Request Data Deletion

 Endpoint to request deletion of personal data.     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = DataPrivacyApi()
val dataPrivacyRequest : DataPrivacyRequest =  // DataPrivacyRequest | 
try {
    apiInstance.requestDeletion(dataPrivacyRequest)
} catch (e: ClientException) {
    println("4xx response calling DataPrivacyApi#requestDeletion")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DataPrivacyApi#requestDeletion")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataPrivacyRequest** | [**DataPrivacyRequest**](DataPrivacyRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

<a id="requestTracking"></a>
# **requestTracking**
> requestTracking(dataPrivacyRequest)

Request Data Tracking

 Endpoint to request tracking of personal data.  Use this to opt back into data tracking after previously requesting deletion.     

### Example
```kotlin
// Import classes:
//import deadlock-api-client.infrastructure.*
//import deadlock-api-client.models.*

val apiInstance = DataPrivacyApi()
val dataPrivacyRequest : DataPrivacyRequest =  // DataPrivacyRequest | 
try {
    apiInstance.requestTracking(dataPrivacyRequest)
} catch (e: ClientException) {
    println("4xx response calling DataPrivacyApi#requestTracking")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DataPrivacyApi#requestTracking")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataPrivacyRequest** | [**DataPrivacyRequest**](DataPrivacyRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

