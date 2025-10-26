# DataPrivacyApi

All URIs are relative to *https://api.deadlock-api.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**requestDeletion**](#requestdeletion) | **POST** /v1/data-privacy/request-deletion | Request Data Deletion|
|[**requestTracking**](#requesttracking) | **POST** /v1/data-privacy/request-tracking | Request Data Tracking|

# **requestDeletion**
> requestDeletion(dataPrivacyRequest)

 Endpoint to request deletion of personal data.     

### Example

```typescript
import {
    DataPrivacyApi,
    Configuration,
    DataPrivacyRequest
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new DataPrivacyApi(configuration);

let dataPrivacyRequest: DataPrivacyRequest; //

const { status, data } = await apiInstance.requestDeletion(
    dataPrivacyRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dataPrivacyRequest** | **DataPrivacyRequest**|  | |


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requestTracking**
> requestTracking(dataPrivacyRequest)

 Endpoint to request tracking of personal data.  Use this to opt back into data tracking after previously requesting deletion.     

### Example

```typescript
import {
    DataPrivacyApi,
    Configuration,
    DataPrivacyRequest
} from 'deadlock-api-client';

const configuration = new Configuration();
const apiInstance = new DataPrivacyApi(configuration);

let dataPrivacyRequest: DataPrivacyRequest; //

const { status, data } = await apiInstance.requestTracking(
    dataPrivacyRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dataPrivacyRequest** | **DataPrivacyRequest**|  | |


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

